class bill :
    def __init__(self,price,product,cust_no,cust_name):
        self.price = 50
        self.product = "soap"

        self._cust_no = input("enter ph no. :")
        self._cust_name = input("enter customer name :")

        self.__revenue = 0

    def bill(self,qty):
        total = self.price * qty
        self.__revenue += total

        print("customer name :",self._cust_name)
        print("customer no. :",self._cust_no)
        print("product name :",self.product)
        print("product amt :",self.price)
        print("product qty :",qty)
        print("total amount :",total)

    def revenues(self):
        print("revenue :",self.__revenue)

bill1 = bill(price = 50,product = "soap",cust_no = "84387xxxxx",cust_name = "Ajay")
bill1.bill(3)

bill1.revenues()
