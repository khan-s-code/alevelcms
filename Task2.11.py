class Toy:

    def __init__(self,name,iD,price,minimum):
        self.__name = name
        self.__iD = iD
        self.__price = price
        self.__minimum = minimum

    
    def Setname(self, n):
        self.__name= n
    def SetiD(self, r):
        self.__iD= r
    def Setprice(self,p):
        self.__price=p
    def Setminimum(self,d):
        self.__minimum=d
    def Getname(self):
        return self.__name
    def GetiD (self):
        return  self.__iD
    def Getprice(self):
        return  self.__price
    def Getminimum(self):
        return  self.__minimum

Toy1 = Toy("Bus","001",13,2)
Toy2 = Toy("Car","002",9,3)
Toy3 = Toy("Train","003",17,4)
Toy4 = Toy("Blocks","004",15,5)

AToys=[Toy1,Toy2,Toy3,Toy4]

def bubbleSort(AToys):
    n = len(AToys)-1
    for i in range(n):
        for j in range(0, n-i):
            if AToys[j].Getprice() > AToys[j+1].Getprice() :
                AToys[j], AToys[j+1] = AToys[j+1], AToys[j]
print( "Before Sorting:")
for r in range (len(AToys)):
    print ("Sorted array is:", AToys[r].Getprice())
bubbleSort(AToys)
print( "After Sorting:")
for r in range (len(AToys)):
    print ("Sorted array is:", AToys[r].Getprice())
