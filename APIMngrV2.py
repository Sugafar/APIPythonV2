import Helpers.NoBase as NB
from Helpers.Temperature import Temp
#from Helpers.CalcFactorsNoBase import NoBase

myTemp = Temp()
enterTemp = (input("Enter the observed Temp in degrees F"))
myTemp.TF90 = float(enterTemp)
myTemp.calcTemps()
print(myTemp.TC90)

#myCalc = NoBase(myTemp)
enterObservedAPIGravity = (input("Enter the observed gravity"))
#myCalc.setAPIGravity(float(enterObservedAPIGravity))

enterPSI = (input("Enter the PSI"))
NB.PSI = float(enterPSI)

NB.setAPIGravity(NB,float(enterObservedAPIGravity))
print(NB.P60)

NB.iterateNewton(NB,myTemp)

#myCalc.iterateNewton()


#print(myCalc.P60Guess)


