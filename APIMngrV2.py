from Helpers.Temperature import Temp
from Helpers.CalcFactorsNoBase import NoBase

myTemp = Temp()
enterTemp = (input("Enter the observed Temp in degrees F"))
myTemp.TF90 = float(enterTemp)
myTemp.calcTemps()
print(myTemp.TC90)

myCalc = NoBase()
enterObservedAPIGravity = (input("Enter the observed gravity"))
myCalc.setAPIGravity(float(enterObservedAPIGravity))

print(myCalc.P60Guess)


