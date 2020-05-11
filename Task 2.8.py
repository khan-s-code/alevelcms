class Toy:

    def __init__(self,name,iD,price,minimum):
        self.__name = name
        self.__iD = iD
        self.__price = price
        self.__minimum = minimum

    def Setprice(self,p):
        self.__price=p
   

    def Getprice(self):
        return  self.__price
    

Toy1 = Toy("Bus","001",13,2)
Toy2 = Toy("Car","002",9,3)
Toy3 = Toy("Train","003",17,4)
Toy4 = Toy("Blocks","004",15,5)

AToys=[Toy1,Toy2,Toy3,Toy4]

def discount (rate):
    for n in range (4):
        price= AToys[n].Getprice()
        price=price-(price* rate/100)
        AToys[n]. Setprice(price)
    

while 1:
    rate= int(input('enter the discount rate'))
    discount(rate)
    print (AToys[1].Getprice())


