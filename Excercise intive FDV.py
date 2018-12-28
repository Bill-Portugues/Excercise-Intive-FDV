


class Rentals:

    # Class designed to handle the whole operation of many different rentals from one specific family or group

    Qrentals = 0            #Counter of Rental Units
    Accumulator = []        #List that groups all the Rental Units

    def __init__(self, Prices, Discount_Rate, Family_Discount):

        self.Prices = Prices                    #Dictionary that stores Type and Price of each category Example {"Hour":5}
        self.Discount_Rate = Discount_Rate      #Percentage to apply in case it triggers the family Discount
        self.Family_Discount = Family_Discount  #List of two elements ([3,5]), first the minimum neccesary and second the maximum possible, to obtaing the discount


    def Add(self, Type, Quantity):

        #Method for adding new Rental Units

        self.Accumulator.append(Rental_Units(Type, Quantity))
        self.Qrentals += 1

    def Overall_Sum(self):

        #Method for calculating and return the overall sum all the rentals added to "Accumulator"

        subtotal = 0
        for rental in self.Accumulator:
            subtotal += self.Prices[rental.Type] * rental.Quantity   #Adding each unit the (Quantity times the Price of the respective Type)

        return subtotal

    def Charging_Price(self):

        # Method for calculating the final Charging Price to the customers

        subtotal = self.Overall_Sum()

        if self.Qrentals >= self.Family_Discount[0] and self.Qrentals <= self.Family_Discount[1]: #Applies the Discount if neccesary
            total = subtotal * (1 - self.Discount_Rate)
        else:
            total = subtotal

        return total #Returning final charging price


class Rental_Units(Rentals):

    #SubClass of Rentals designed to handle each rental unit individually


    def __init__(self, Type, Quantity):
        self.Type = Type            #Periodic time of the rental (Hour, Day, Week, etc)
        self.Quantity = Quantity    #Specific amount of the rental type (How many days, weeks, etc)


def Api():
    #Application example of how to manipulate the Rental Class

    #Declaring the Variable Values needed for this specific case
    Options = {"H": "Hours", "D": "Days", "W": "Weeks"}
    Prices = {"Hours": 5, "Days": 20, "Weeks": 60}
    Discount_Rate = 0.3
    Family_Discount = [3, 5]


    Model = Rentals(Prices, Discount_Rate, Family_Discount) #Initialize a new instance of Rentals
    Flag = "Y"

    while Flag=="Y":         #Each iteration gives you the possibility of adding a new rental unit or ending the process

        Type = GetString("Enter the Rental Type that you wish: H = Hour, D = Day, W = Week:",Options)
        Quantity = GetInt("Enter the quantity of " + Options[Type] + " you wish:",0)
        Model.Add(Options[Type], Quantity)    #Initializing a new instance of rental units
        Flag = GetString(" Do you want to add a new Rental? Y=Yes , N=No:",["Y","N"])

    print("The final Value for the %d rentals is of $ %.2f" % (Model.Qrentals, Model.Charging_Price()))


def GetString(Question,Options):
    #Function that receives Question and possible answers and return the selected one.

    answer = input("\n " + Question + " \n --> ").upper()

    while not(answer in Options):
        answer = input("\n "+ "Respuesta Incorrecta, Vuelva a intentarlo" + " \n --> ").upper()


    return answer   #Always returns string in uppercase


def GetInt(Question, Restriction):

    # Function that receives Question and Minimum restriction and returns integer.

    answer = input("\n " + Question + " \n --> ")                   #input returns string

    while  not(answer.isdigit() and int(answer) >=Restriction):     #.isdigit() checks if the string is a number
        answer = input("\n " + "Respuesta Incorrecta, Vuelva a intentarlo" + " \n --> ")

    return int(answer)

Api()
