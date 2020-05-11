class Toy:
    def __init__ (self,name,Id,price,minimumage):
        self.name=name
        self.Id=Id
        self.price=price
        self.minimumage=minimumage
    def getname(self):
        return self.name
toy1=Toy("train","004",45,3)
toy2=Toy("sheep","112",500,6)
toy3=Toy("car","111",300,10)

toyarray=[toy1,toy2,toy3]

def search(ID):
    found = False
    for n in range (3):
        if  toyarray[n].Id==ID:
            print (toyarray[n].name,toyarray[n].price,toyarray[n].minimumage)
            found=True
    if found==False:
        print("not found")

while 1:
    searchid=input("enter ID to search")
    search(searchid)
    
        
            
