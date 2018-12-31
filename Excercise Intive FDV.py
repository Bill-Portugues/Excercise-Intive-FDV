

class AdministratorOfRentalGroupOrders:

    # Class designed to handle the whole operation of many different rentals from one specific family or group

    CounterOfRentalUnits = 0
    ListOfAllRentalUnitsInstances = []

    def __init__(self, RentalTypePrices, FamilyDiscountRate, FamilyDiscountRange):

        self.RentalTypePrices = RentalTypePrices         #Dictionary that stores Type and Price of each category Example {"Hour":5}
        self.FamilyDiscountRate = FamilyDiscountRate     #Percentage to apply in case it triggers the family Discount
        self.FamilyDiscountRange = FamilyDiscountRange  #List of two elements ([3,5]), first the minimum neccesary and second the maximum possible, to obtaing the discount


    def AddNewRental(self, PeriodicRentalType, PeriodicQuantity):

        #Method for adding new RentalUnits

        self.ListOfAllRentalUnitsInstances.append(RentalUnits(PeriodicRentalType, PeriodicQuantity))
        self.CounterOfRentalUnits += 1

    def OverallSumRentals(self):

        #Method for calculating and return the overall sum all the rentals added to "Accumulator"

        subtotal = 0
        for rental in self.ListOfAllRentalUnitsInstances:
            subtotal += self.RentalTypePrices[rental.PeriodicRentalType] * rental.PeriodicQuantity   #Adding each unit the (Quantity times the Price of the respective Type)

        return subtotal

    def ChargingPrice(self):

        # Method for calculating the final Charging Price to the customers

        subtotal = self.OverallSumRentals()

        if self.CounterOfRentalUnits >= self.FamilyDiscountRange[0] and \
                self.CounterOfRentalUnits <= self.FamilyDiscountRange[1]:
            total = subtotal * (1 - self.FamilyDiscountRate)
        else:
            total = subtotal

        return total #Returning final charging price


class RentalUnits(AdministratorOfRentalGroupOrders):

    #SubClass of AdministratorOfRentalGroupOrders designed to handle each rental unit individually


    def __init__(self, PeriodicRentalType, PeriodicQuantity):
        self.PeriodicRentalType = PeriodicRentalType #Periodic time of the rental (Hour, Day, Week, etc)
        self.PeriodicQuantity = PeriodicQuantity     #Specific amount of the rental type (How many days, weeks, etc)


class Test():

    # Declaring the Variable Values needed for this specific case
    RentalTypePrices = {"Hours": 5, "Days": 20, "Weeks": 60}
    FamilyDiscountRate = 0.3
    FamilyDiscountRange = [3, 5]

    def __init__(self):

        self.TestCase=AdministratorOfRentalGroupOrders(self.RentalTypePrices, self.FamilyDiscountRate, self.FamilyDiscountRange)

    def reset(self):

        self.TestCase.ListOfAllRentalUnitsInstances=[]
        self.TestCase.CounterOfRentalUnits = 0

    def InitializationTest(self):


        assert len(self.TestCase.FamilyDiscountRange)==2,"The Family Discount Range has more or less than 2 values"
        assert isinstance((self.TestCase.FamilyDiscountRate),float),"Family Discount Rate is not a data float"
        assert len(self.TestCase.RentalTypePrices)!=0, "Rental Type Prices is empty"

        self.reset()

    def AddNewRentalTest(self,TestList):


        assert len(self.TestCase.ListOfAllRentalUnitsInstances)==0,"ListOfAllRentalUnitsInstances is not initialize empty"

        for sample in TestList:
            self.TestCase.AddNewRental(sample[0], sample[1])

        assert len(self.TestCase.ListOfAllRentalUnitsInstances)==len(TestList),"ListOfAllRentalUnitsInstances is not adding properly new RentalUints"

        self.reset()

    def RentalUnitsIntegrityTest(self,TestList):

        counter=0
        for sample in TestList:

            self.TestCase.AddNewRental(sample[0], sample[1])

            assert self.TestCase.ListOfAllRentalUnitsInstances[counter].PeriodicRentalType==sample[0],"Wrong pass through of parameters to Rental unit"
            assert self.TestCase.ListOfAllRentalUnitsInstances[counter].PeriodicQuantity==sample[1],"Wrong pass through of parameters to Rental unit"
            counter+=1

        self.reset()

    def OverallSumRentalsTest(self,TestList):

        subtotal=0

        for sample in TestList:
            self.TestCase.AddNewRental(sample[0], sample[1])

            subtotal+=sample[1] * self.RentalTypePrices[sample[0]]

            assert self.TestCase.OverallSumRentals() == subtotal, "OverallSumRentals is summing incorrectly"


        self.reset()

    def ChargingPriceTest(self,TestList):

        subtotal = 0

        for sample in TestList:
            self.TestCase.AddNewRental(sample[0], sample[1])

            subtotal += sample[1] * self.RentalTypePrices[sample[0]]

        if len(TestList)>=self.FamilyDiscountRange[0] and len(TestList)<=self.FamilyDiscountRange[1]:
            total = subtotal * (1-self.FamilyDiscountRate)
        else:
            total=subtotal

        assert self.TestCase.ChargingPrice() == total, "ChargingPrice is giving the wrong result"

        self.reset()




TestSamples1=[["Weeks",4],["Hours",5]] # 2 Rental Units
TestSamples2=[["Hours",1],["Hours",0],["Hours",2]] # 3 Rental Units
TestSamples3=[["Days",9],["Days",5],["Days",14],["Weeks",3],["Days",0]] # 5 Rental Units
TestSamples4=[["Weeks",4],["Hours",5],["Days",8],["Weeks",3],["Days",0],["Weeks",33],["Weeks",9]] # 7 Rental Units

TestSamples=[TestSamples1,TestSamples2,TestSamples3,TestSamples4]


TestCase=Test()
TestCase.InitializationTest()

for samples in TestSamples:

    TestCase.AddNewRentalTest(samples)
    TestCase.RentalUnitsIntegrityTest(samples)
    TestCase.OverallSumRentalsTest(samples)
    TestCase.ChargingPriceTest(samples)

print ("\n All Test were executed properly")