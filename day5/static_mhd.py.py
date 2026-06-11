class bill :
    def __init__(self,price,product,cust_no,cust_name):
        self.price = 50
        self.product = "soap"

        self._cust_no = input("enter ph no. :")
        self._cust_name = input("enter customer name :")

    @staticmethod
    def change_price(self,new_price,new_no):
        self.price = new_price
        self._cust_no = new_no

bill1 = bill(price = "",product = "",cust_no = "",cust_name = "Ajay")
print(bill1.price)
print(bill1._cust_no)
bill1.change_price(bill1, 40,98652)
print(bill1.price)
print(bill1._cust_no)