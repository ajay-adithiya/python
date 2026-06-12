class store:
    def __init__(self):
        self.__revenue = 70000

    @property
    def Revenue(self):
        return self.__revenue
    
    @Revenue.setter
    def change_revenue(self,new_revenue):
        if new_revenue > 0:
            self.__revenue = new_revenue
            return self.__revenue
    
    @Revenue.deleter 
    def del_Revenue(self):
        del self.__revenue

class income(store):
    def Income(self):
        return self.__revenue
    
class new_income(store):
    def nincome(self,new_revenue):
        return self.__revenue
    
st = income()
print(st.Revenue)

str = new_income()
str.nincome = 80000
print(str.nincome)

delt = store()
del delt.del_Revenue

print(st.Revenue)