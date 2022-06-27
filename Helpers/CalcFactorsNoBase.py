
class NoBase:
    def __init__(self):
        self.APIGravity = float(0.0)
        self.P60Guess = float(0.0)
        self. NextGuess = float(0.0)
        self.DensityMin = float(610.6)
        self.DensityMax = float(1163.5)
        self.K0 = float(341.0957)
        self. K1 = float(0.0)
        self.K2 = float(0.0)
        self.Da = float(2.0)
        self.HasDiverged = bool(False)
        #IsProduct = Boolean(false)

        # Density at alternate conditions
        self.PO = float(0.0)

        self.PSI = float(0.0)

        #PSI2 another psi for convertting to alternate conditions
        self.PSI2 = float(0.0)

        #temp at alternate conditions, I'm just going to use the TempObj
        #T = float(0.0)

        # another temp for converting to an alternate condition
        self.T2 = float(0.0)

        #Set this to true if PSI2 and T2 are used
        self.CalculateVolumeAtAltTempAndPSI = bool(False)

        #begin intermediate values

        #Temperature Shift value
        self.S60 = float(0.01374979547)

        #Alternate temperature shifted to IPTS-68 basis (F)
        self.TStar = float(0.0)

        #Base density shifted to IPTS-68 60F basis
        self.PStar = float(0.0)

        # Alternate Tempterature - base temperature of 60 degrees F
        self.ChangeT = float(0.0)

        #Coefficient in correlation for a60
        self.K0 = float(0.0)

        # Coefficient in correlation for a60
        self.K1 = float(0.0)

        # Coefficient in correlation for a60
        self.K2 = float(0.0)

        #Variable used in calculation of pStar
        self.A = float(0.0)

        # Variable used in calculation of pStar
        self.B = float(0.0)

        #Variables used to check range excursion
        self.DrMin = float(0.0)
        self.DrMax = float(0.0)

        self.Rho60 = float(0.0)

        #Correction factor due to density used in iterative procedure
        self.E = float(0.0)

        #Coefficient needed to perform iteration on p60
        self.Da = float(0.0)

        #Correction factor due to temperature used in iterative procedure
        self.Dt = float(0.0)

        #Correction factor due to pressure used in iterative procedure
        self.Dp = float(0.0)

        #

        #Hydrometer Correction Factor
        self.HYC = float(0.0)

        #end intermediate values

        #begin output values

        #Volume correction factor due to temperature
        self.CTL = float(0.0)

        #Volume correction factor due to pressure
        self.CPL = float(0.0)

        # Scaled compressibility factor
        self.Fp = float(0.0)

        #Combined volume corection factor due to temperature and pressure
        self.CTPL = float(0.0)

        #Density at alternate conditions
        self.P = float(0.0)

        #Volume at base conditions (60F and 0 PSI)
        self.V60 = float(0.0)

        #end output values

     #setAPIGravity converts
    #  API Gravity to a Density value in kg/cubic meter.
    #  This converted value becomes p60Guess and po
    def setAPIGravity(self,value):
        self.P60Guess = (141.5 / (value + 131.5)) * 999.016
        self.PO = (141.5 / (value + 131.5)) * 999.016
        self.APIGravity = value