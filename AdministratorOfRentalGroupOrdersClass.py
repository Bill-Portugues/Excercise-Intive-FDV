
class AdministratorOfRentalGroupOrders:

    # Class designed to handle the whole operation of many different rentals from one specific family or group

    CounterOfRentalUnits = 0
    ListOfAllRentalUnitsInstances = []

    def __init__(self, RentalTypePrices, FamilyDiscountRate, FamilyDiscountRange):

        self.RentalTypePrices = RentalTypePrices         #Dictionary that stores Type and Price of each category Example {"Hour":5}
        self.FamilyDiscountRate = FamilyDiscountRate     #Percentage to apply in case it triggers the family Discount
        self.FamilyDiscountRange = FamilyDiscountRange   #Range [Min,Max], first the minimum neccesary and second the maximum possible, to obtain the discount


    def AddNewRental(self, PeriodicRentalType, PeriodicQuantity):

        #Method for adding new RentalUnits

        self.ListOfAllRentalUnitsInstances.append(RentalUnits(PeriodicRentalType, PeriodicQuantity))
        self.CounterOfRentalUnits += 1

    def OverallSumRentals(self):

        #Method for calculating and return the overall summing all the rentals added to "ListOfAllRentalUnitsInstances"

        subtotal = 0
        for rental in self.ListOfAllRentalUnitsInstances:
            subtotal += self.RentalTypePrices[rental.PeriodicRentalType] * rental.PeriodicQuantity   #Price times Quantity for each unit

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
        self.PeriodicQuantity = PeriodicQuantity     #Specific amount of the PeriodicRentalType (How many days, weeks, etc)

