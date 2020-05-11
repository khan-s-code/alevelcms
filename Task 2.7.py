class Toy:

    def __init__(self,name,iD,price,minimum):
        self.__name = name
        self.__iD = iD
        self.__price = price
        self.__minimum = minimum

    def Getname(self):
        return self.__name
    def GetiD (self):
        return self.__iD
    def Getprice(self):
        return self.__price
    def Getminimum(self):
        return self.__minimum

Toy1 = Toy("Bus","001",13,2)
Toy2 = Toy("Car","002",9,3)
Toy3 = Toy("Train","003",17,4)
Toy4 = Toy("Blocks","004",15,5)

AToys=[Toy1,Toy2,Toy3,Toy4]

def search (iD):
    Found = False
    for n in range (4):
        if AToys[n]. GetiD ()==iD:
            print(AToys[n].Getname(),AToys[n].GetiD(),AToys[n].Getprice(),AToys[n].Getminimum())
            Found = True
    if Found == False:
        print("The Toy is not found")

while True:
   searchiD=input("Enter the ID you want to search")
   search(searchiD)
        
