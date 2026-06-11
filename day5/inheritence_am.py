# protected
class bill:
    def __init__(self):
        self._cust_name = "ajay"

    def income(self): # protected
        self.__revenue = 50000
        print(self.__revenue)
        
class cust(bill):
    def show(self):
        print(self._cust_name)
        
Bill = cust()
Bill.show()

Income = bill()
Income.income()

