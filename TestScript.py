import TestClass

#Set of different Samples to check all important aspects of the object under study

TestSamples1=[["Weeks",4],["Hours",5]] # 2 Rental Units
TestSamples2=[["Hours",1],["Hours",0],["Hours",2]] # 3 Rental Units
TestSamples3=[["Days",9],["Days",5],["Days",14],["Weeks",3],["Days",0]] # 5 Rental Units
TestSamples4=[["Weeks",4],["Hours",5],["Days",8],["Weeks",3],["Days",0],["Weeks",33],["Weeks",9]] # 7 Rental Units

TestSamples=[TestSamples1,TestSamples2,TestSamples3,TestSamples4]


TestCase=TestClass.Test({"Hours": 5, "Days": 20, "Weeks": 60},0.3,[3, 5])                 #initializing object under study
TestCase.InitializationTest()

for samples in TestSamples:

    TestCase.AddNewRentalTest(samples)
    TestCase.RentalUnitsIntegrityTest(samples)
    TestCase.OverallSumRentalsTest(samples)
    TestCase.ChargingPriceTest(samples)

print ("\n All Test were executed properly")