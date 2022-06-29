from Helpers.Temperature import Temp
import math

K0 = 341.0957
K1 = 0.0
K2 = 0.0
Da = 2.0
APIGravity = 0.0
# Density at base conditions (60F and 0 PSI). 
P60 = 0.0

#setAPIGravity converts
#  API Gravity to a Density value in kg/cubic meter.
#  This converted value becomes p60Guess and po
def setAPIGravity(self,value):
    self.APIGravity = value
    self.P60 = (141.5 / (value + 131.5)) * 999.016

DensityMin = 610.6
DensityMax = 1163.5

PSI = 0.0

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

def calculate(self,Temp):
    myTemp = Temp

    self.A = (self.S60 / 2) * ((self.K0 / self.P60 + self.K1) * 1 / self.P60 + self.K2)
    self.B = (2 * self.K0 + self.K1 * self.P60) / (self.K0 + (self.K1 + self.K2 * self.P60) * self.P60)

    p1 = math.exp(self.A * (1 + 0.8 * self.A)) - 1
    p2 = 1 + self.A * (1 + 1.6 * self.A) * self.B
    self.PStar = self.P60 * (1 + (p1 / p2))


    a60 = (self.K0 / self.PStar + self.K1) * 1 / self.PStar + self.K2  

    #Calc CTL
    cf1 = (-1 * a60 * myTemp.ChangeT)
    cf2 = (myTemp.ChangeT + self.S60)
    cf3 = math.exp(cf1 * cf2)
    self.CTL = math.exp(-a60 * myTemp.ChangeT * (1 + (.8 * a60) * (myTemp.ChangeT + self.S60)))

    #Calc CPL
    Fpa = -1.9947 + (0.00013427 * myTemp.TF68)
    Fpb = ((793920 + 2326 * myTemp.TF68) / (pow(self.PStar, 2)))
    Fp = math.exp(Fpa + Fpb)
    self.CPL = 1 / (1 - (math.pow(10, -5) * Fp * (self.PSI)))



