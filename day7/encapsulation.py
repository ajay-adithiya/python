class Bill:

    def __init__(self, customer_name, phone):
        self._customer_name = customer_name
        self._phone = phone

        self.name = "Soap"
        self.price = 40

        self.__revenue = 0

    def sell(self, quantity):

        amount = self.price * quantity
        self.__revenue += amount
        print("Amount =", amount)

    def show(self):
        print("Revenue =", self.__revenue)

    def get_revenue(self):      # getter method
        return self.__revenue 
    
    def set_revenue(self,amount):
        self.__revenue = amount
        return self.__revenue

class revenue(Bill):
    def getrevenue(self):      # getter method
        return self.__revenue 

bill = Bill("Ajay", "84387xxxxx")
bill.sell(5)
bill.show()

print(bill.get_revenue())

print(bill.set_revenue(20000))

bills = revenue("Ajay", "84387xxxxx")
bills.get_revenue()