# python 3.5.2


class Rental_Type:
    def __init__(self, Type, Quantity):

        self.Type = Type
        self.Quantity = Quantity

class Rentals:

    def __init__(self, Prices, Discount_Rate, Family_Discount):
        self.Accumulator = []
        self.Prices = Prices
        self.Discount_Rate = Discount_Rate
        self.Family_Discount = Family_Discount
        self.Qrentals = 0

    def Add(self, Type, Quantity):

        self.Accumulator.append(Rental_Type(Type, Quantity))
        self.Qrentals += 1

    def Charging_Price(self):

        subtotal = 0
        for rental in self.Accumulator:
            subtotal += self.Prices[rental.Type] * rental.Quantity

        if self.Qrentals >= self.Family_Discount[0] and self.Qrentals <= self.Family_Discount[1]:
            total = subtotal * (1 - self.Discount_Rate)
        else:
            total = subtotal

        return total


def Api():
    Options = {"H": "Hours", "D": "Days", "W": "Weeks"}
    Prices = {"Hours": 5, "Days": 20, "Weeks": 60}
    Discount_Rate = 0.3
    Family_Discount = [3, 5]

    Model = Rentals(Prices, Discount_Rate, Family_Discount)
    Flag = True

    while Flag:

        Type = input("\n Enter the Rental Type that you wish: H = Hour, D = Day, W = Week: \n --> ").upper()
        Quantity = int(input("\n Enter the quantity of " + Options[Type] + " you wish: \n --> "))
        Model.Add(Options[Type], Quantity)

        Continue = input("\n Do you want to add a new Rental? Y=Yes , N=No: \n --> ").upper()
        if Continue == "N": Flag = False

    print("The final Value for the %d rentals is of $ %f" % (Model.Qrentals, Model.Charging_Price()))

Api()
