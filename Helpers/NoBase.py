
from Helpers.Temperature import Temp
import math

K0 = 341.0957
K1 = 0.0
K2 = 0.0
Da = 2.0
P60Guess = 0.0
APIGravity = 0.0
NextGuess = 0.0
DensityMin = 610.6
DensityMax = 1163.5
HasDiverged = False

# Density at alternate conditions
P0 = 0.0

# Density at base conditions (60F and 0 PSI). 
P60 = 0.0

PSI = 0.0

#PSI2 another psi for convertting to alternate conditions
PSI2 = 0.0

# another temp for converting to an alternate condition
T2 = 0.0

#Set this to true if PSI2 and T2 are used
CalculateVolumeAtAltTempAndPSI = bool(False)

#begin intermediate values

#Temperature Shift value
S60 = 0.01374979547

#Alternate temperature shifted to IPTS-68 basis (F
TStar = 0.0

#Base density shifted to IPTS-68 60F basis
PStar = 0.0

# Alternate Tempterature - base temperature of 60 degrees F
ChangeT = 0.0

#Variable used in calculation of pStar
A = 0.0

# Variable used in calculation of pStar
B = 0.0

#Variables used to check range excursion
DrMin = 0.0
DrMax = 0.0

Rho60 = 0.0

#Correction factor due to density used in iterative procedure
E = 0.0

#Coefficient needed to perform iteration on p60
Da = 0.0

#Correction factor due to temperature used in iterative procedure
Dt = 0.0

#Correction factor due to pressure used in iterative procedure
Dp = 0.0

# Variable used in calculation of pStar
A = 0.0

# Variable used in calculation of pStar
B = 0.0

#Hydrometer Correction Factor
HYC = 0.0

#end intermediate values

#begin output values

#Volume correction factor due to temperature
CTL = 0.0

#Volume correction factor due to pressure
CPL = 0.0

# Scaled compressibility factor
Fp = 0.0

#Combined volume corection factor due to temperature and pressure
CTPL = 0.0

#Density at alternate conditions
P = 0.0

#Volume at base conditions (60F and 0 PSI
V60 = 0.0

#A60 = 0.0

#end output values

#setAPIGravity converts
#  API Gravity to a Density value in kg/cubic meter.
#  This converted value becomes p60Guess and po
def setAPIGravity(self,value):
    self.P60Guess = (141.5 / (value + 131.5)) * 999.016
    self.P0 = (141.5 / (value + 131.5)) * 999.016
    self.APIGravity = value
    self.P60 = (141.5 / (value + 131.5)) * 999.016

#Runs Newton's Iteration searching for truth or something close
def iterateNewton(self,Temp):
    myTemp = Temp
    M = 1
    counter = int(0)

    while(counter<16):
        # important part of calcCV goes here
        if self.HYC == 0.0:
           self.HYC = 1 - (0.00001278 * (myTemp.TF90 - 60)) - ((0.0000000062 * pow((myTemp.TF90 - 60), 2)))
           self.P60Guess = self.P60Guess * self.HYC
           self.P0 = self.P0 * self.HYC

        self.A = (self.S60 / 2) * ((self.K0 / self.P60Guess + self.K1) * 1 / self.P60Guess + self.K2)
        self.B = (2 * self.K0 + self.K1 * self.P60Guess) / (self.K0 + (self.K1 + self.K2 * self.P60Guess) * self.P60Guess)

       # p1 = (self.A ** (1 + 0.8 * self.A)) - 1
        p1 = math.exp(self.A * (1 + 0.8 * self.A)) - 1
        p2 = 1 + self.A * (1 + 1.6 * self.A) * self.B
        self.PStar = self.P60Guess #* (1 + (p1 / p2))

        a60 = (self.K0 / self.PStar + self.K1) * 1 / self.PStar + self.K2  
        
        
        #Calc CTL
        cf1 = (-1 * a60 * myTemp.ChangeT)
        cf2 = (myTemp.ChangeT + self.S60)
        cf3 = (cf1 ** cf2)

        #print("cf3" + str(cf3))

        self.CTL = math.exp(-a60 * myTemp.ChangeT * (1 + (.8 * a60) * (myTemp.ChangeT + self.S60)))
        #self.CTL = (-self.A60 * myTemp.ChangeT) ** (1 + (.8 * self.A60) *  (myTemp.ChangeT + self.S60))
        #print("CTL " + str(self.CTL))
        #Calc Fp
        #double Fpa, Fpb;  //used to clarify the equation
        Fpa = -1.9947 + (0.00013427 * self.TStar)
        Fpb = ((793920 + 2326 * self.TStar) / (pow(self.PStar, 2)))

        Fp = math.exp(Fpa + Fpb)

        self.CPL = 1 / (1 - (math.pow(10, -5) * Fp * (self.PSI)))

        CTPL = self.CTL * self.CPL

        Rho60mXCTPlm = self.P60Guess * CTPL
        DeltaRho60m = Rho60mXCTPlm - self.P0
        Sp0 = abs(DeltaRho60m)

        if (Sp0 < 0.000001):
            print('How many loops: ' + str(counter))
            print('CTL: ' + str(self.CTL))
            print('CPL: ' + str(self.CPL))
            correctedGravity = (141.5 / (self.P60Guess / 999.016)) - 131.5
            print('Corrected Gravity @60: ' + str(correctedGravity))
            break

        # if it didn't break it needs another round, so here's the factors needed to generate the next quess
        E = (self.P0 / (CTPL)) - self.P60Guess
        self.Dt = self.Da * a60 * myTemp.DeltaT * (1 + (1.6 * a60 * myTemp.DeltaT))
        dp1 = 2 * self.CPL * self.PSI * Fp
        dp2 = 7.93920 + (0.02326 * myTemp.TF90)
        self.Dp = -(dp1 * dp2) / (self.P60Guess * self.P60Guess)
        changeP60 = E / (1 + self.Dt + self.Dp)

        self.P60Guess = self.P60Guess + changeP60
        counter = counter + 1

        #print(self.P60Guess)
