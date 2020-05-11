class Toy():

    def __init__(self,name,iD,price,minimum):
        self.__name = name
        self.__iD = iD
        self.__price = price
        
        if not( minimum >0 and minimum <19):
            raise Exception(" Age must between 0-18")
        self.minimum = minimum
ThisToy=Toy("Red Sports Car","RSC13",15.00,190)
ThatToy=Toy("Red Sports Car","RSC13",15.00,14)
print(ThatToy.minimum)

