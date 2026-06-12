class payment:
    def pay(self,amount):
        pass

class UPI(payment):
    def pay(self,amount):
        print(f"{amount},paid through UPI")

class CASH(payment):
    def pay(self,amount):
        print(f"{amount},paid as cash")

class CARD(payment):
    def pay(self,amount):
        print(f"{amount},paid using card")

paid = [UPI(),CASH(),CARD()]
for pays in paid:
    pays.pay(500)