
import AdministratorOfRentalGroupOrdersClass


class Test():

    # Setting up the Variable parametrized for this specific case


    def __init__(self,RentalTypePrices,FamilyDiscountRate,FamilyDiscountRange):

        # Creating an instance of the object under testing
        self.TestCase=AdministratorOfRentalGroupOrdersClass.AdministratorOfRentalGroupOrders(RentalTypePrices, FamilyDiscountRate, FamilyDiscountRange)
        self.RentalTypePrices = RentalTypePrices
        self.FamilyDiscountRate = FamilyDiscountRate
        self.FamilyDiscountRange = FamilyDiscountRange


    def reset(self):

        #Method for returning the object to its original state
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



