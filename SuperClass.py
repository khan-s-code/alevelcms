class Person:

    def __init__(self,first,last):
        self.__firstname = first
        self.__lastname = last
        self.__age = 0
    def SetAge(self,a):
        self.__age = a
    def GetAge(self):
        return self.__age


    def __str__(self):
        return self.__firstname + " " + self.__lastname + ", " + str(self.__age)

class Employee(Person):

    def __init__(self, first, last, staffnum):
        super().__init__(first, last)
        self.staffnumber = staffnum

    def __str__(self):
        return super().__str__() + ", " +  self.staffnumber


x = Person("Marge", "Simpson")
x.SetAge(36)
print(x.GetAge())
#y = Employee("Homer", "Simpson", 28, "1007")

#print(x)
#print(y)
#print(x.firstname)

file = open("Records.txt", 'w')

file.write(x.__str__())

file.close()
