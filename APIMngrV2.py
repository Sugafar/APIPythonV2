from imp import reload
import Helpers.NoBase as NB
import Helpers.Base as B
from Helpers.Temperature import Temp

#begin getting base density
myTemp = Temp()
enterTemp = (input("Enter the observed Temp in degrees F "))
myTemp.TF90 = float(enterTemp)
myTemp.calcTemps()

enterObservedAPIGravity = (input("Enter the observed gravity "))

enterPSI = (input("Enter the PSI "))
NB.PSI = float(enterPSI)

NB.setAPIGravity(NB,float(enterObservedAPIGravity))
NB.calculate(NB,myTemp)
myBaseGravity = round(NB.BaseGravity,1)
#end getting base density

#new up a Temp object for the meter
myMeterTemp = Temp()
enterMeterTemp = (input("Enter the Avg Meter Temp in degrees F "))
myMeterTemp.TF90 = float(enterMeterTemp)
myMeterTemp.calcTemps()

enterMeterPSI = (input("Enter the Avg Meter PSI "))
B.PSI = float(enterMeterPSI)
B.setAPIGravity(B,myBaseGravity)
B.calculate(B,myMeterTemp)
CTLm = B.CTL
CPLm = B.CPL

#reload B
reload(B)
#new up a Temp object for the prover
myProverTemp = Temp()
enterProverTemp = (input("Enter the Avg Prover Temp in degrees F "))
myProverTemp.TF90 = float(enterProverTemp)
myProverTemp.calcTemps()

enterProverPSI = (input("Enter the Avg Prover PSI "))
B.PSI = float(enterProverPSI)
B.setAPIGravity(B,myBaseGravity)
B.calculate(B,myProverTemp)
CTLp = B.CTL
CPLp = B.CPL

print('')
print('Corrected Gravity @ 60 F: ' + str(round(myBaseGravity,1)))
print('')


print('CTLm: ' + str(round(CTLm,5)))
print('CPLm: ' + str(round(CPLm,5)))

print('')
print('CTLp: ' + str(round(CTLp,5)))
print('CPLp: ' + str(round(CPLp,5)))
print('')




