class Temp:
    def __init__(self):
        self.TF90 = float(0.0)
         #intermediate variables
        self.TC90 = float(0.0)

        #Correction to ITS-90 temperatue to give IPTS-68 temperature (C)
        self.DeltaT = float(0.0)

        #Scaled temperature value
        self.T = float(0.0)

        #end intermediate variables

        #output variables

        #Temperature consistent with IPTS-68 (F)
        self.TF68 = float(0.0)

        #Temperature consistent with IPTS-68 (C)
        self.TC68 = float(0.0)

        #I added this to move it out of the iteration loop
        self.ChangeT = 0

    def calcTemps(self):
        # convert input F to input C
        self.TC90 = (self.TF90 - 32) / 1.8

        #Calculate the scaled temperature value
        self.T = self.TC90 / 630

            #Calc the temperature correction
        self.DeltaT = (-0.148759 + (-0.267408 + (1.080760 + (1.269056 + (-4.089591 + (-1.871251 + (7.438081 + (-3.536296 * self.T)) * self.T) * self.T) * self.T) * self.T) * self.T) * self.T) * self.T

            #/Determine the equivalent IPTS-68 Temp. We probably won't use this

        self.TC68 = self.TC90 - self.DeltaT

        #Convert back to F
        self.TF68 = 1.8 * self.TC68 + 32

        # moved here from iteration loop
        self.ChangeT = self.TF68 - 60.0068749

        print(self.ChangeT)