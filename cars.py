class VEHICLES:
    def __init__(self,type, price):
        self.type = type
        self.price = price

    def __str__(self):
        return(f"This car is a {self.type} and it's worth {self.price}")
Benz = VEHICLES("Red Convertible", "600000")
Toyota = VEHICLES("Blue Van", "1000000")
print(Benz)
print(Toyota)

