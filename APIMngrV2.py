from imp import reload
import Helpers.NoBase as NB
import Helpers.Base as B
from Helpers.Temperature import Temp

#begin getting base density
myTemp = Temp()
enterTemp = (input("Enter the observed Temp in degrees F"))
myTemp.TF90 = float(enterTemp)
myTemp.calcTemps()


#myCalc = NoBase(myTemp)
enterObservedAPIGravity = (input("Enter the observed gravity"))
#myCalc.setAPIGravity(float(enterObservedAPIGravity))

enterPSI = (input("Enter the PSI"))
NB.PSI = float(enterPSI)

NB.setAPIGravity(NB,float(enterObservedAPIGravity))
#print(NB.P60)


NB.calculate(NB,myTemp)
myBaseGravity = round(NB.BaseGravity,1)


#end getting base density

#new up a Temp object for the meter
myMeterTemp = Temp()
enterMeterTemp = (input("Enter the Avg Meter Temp in degrees F"))
myMeterTemp.TF90 = float(enterMeterTemp)
myMeterTemp.calcTemps()

enterMeterPSI = (input("Enter the Avg Meter PSI"))
B.PSI = float(enterMeterPSI)
print('')
print('Corrected Gravity @ 60 F: ' + str(round(myBaseGravity,1)))
print('')

B.setAPIGravity(B,myBaseGravity)
B.calculate(B,myMeterTemp)
print('CTLm: ' + str(round(B.CTL,5)))
print('CPLm: ' + str(round(B.CPL,5)))
print('')




