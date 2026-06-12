from abc import ABC , abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class UPI(payment):
    def pay(self,amount):
        print(f"{amount} payment through UPI")

class cash(payment):
    def pay(self,amount):
        print(f"{amount} paid as cash")

class card(payment):
    def pay(self,amount):
        print(f"{amount} paid through card")

transaction = [UPI(),cash(),card()]
for amt in transaction:
    amt.pay(500)