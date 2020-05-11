class Toy(object):

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
    #def Setminimum(self,d):
        #self.__minimum=d
    @ property
    def minimum (self):
        return self.__minimum
    @minimum.setter
    def Setminimum (self,minimum):
        if not( minimum >0 and minimum <19):
            raise Exception(" Age must between 0-18")
        self.__minimum = minimum
    

    def Getname(self):
        return self.__name
    def GetiD (self):
        return  self.__iD
    def Getprice(self):
        return  self.__price
    def Getminimum(self):
        return  self.__minimum
    
class ComputerGame(Toy):

    def __init__(self,name,iD,price,minimum,category,console):
        super().__init__(name,iD,price,minimum)
        self.__category=category
        self.__console=console

    def Setcategory(self, a):
        self.__category=a
    def Setconsole(self):
        self.__console=0
    def Getcategory(self):
        return (self.__category)
    def Getconsole(self):
        return (self.__console)

class Vehicle (Toy):

    def __init__(self,name,iD,price,minimum,Type,height,length,weight):
        super().__init__(name,iD,price,minimum)
        self.__Type=Type
        self.__height=height
        self.__length=length
        self.__weight=weight
        
    def SetType(self,t):
        self.__Type=t
    def Setheight(self,h):
        self.__height=h
    def Setlength(self,l):
        self.__length=l
    def Setweight(self,w):
        self.__weight=w
    def GetType(self):
        return(self.__Type)
    def Getheight(self):
        return (self.__height)
    def Getlength(self):
        return (self.__length)
    def Getweight(self):
        return (self.__weight)
    
       
ThisVehicle=Vehicle("Red Sports Car","RSC13",15.00,19,"Car",3.3,12.1,0.08)
#print (ThisVehicle.Getname())
#print (ThisVehicle.Getlength())
#ThisVehicle.Setname("Red Car")
#print (ThisVehicle.Getname( ))
ThisVehicle.Setminimum("19")
print(ThisVehicle.minimum())
