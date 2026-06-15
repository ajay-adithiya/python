class mysecret():

    def __init__(self,key):
        self.__api_key = key

    def getkey(self):
        return self.__api_key
    
s1  = mysecret("keyADITYA@123")
print(s1.getkey())