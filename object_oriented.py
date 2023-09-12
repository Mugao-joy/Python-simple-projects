#exericse 1: pet class
#have the following attributes: __init__, setname,setanimaltype, setage, getname, get animaltype,getage, __str__

class Pet:
    def __init__(self):
        self.__name = "No Name"
        self.__animaltype = "No Type"
        self.__age = 0
#end class

#mutator methods

def setName(self, name):
    self.__name = name
def setAnimalType(self, animalType):
    self.__animalType = animalType
def setAge(self, Age):
    self.__Age = Age
#end method

#accessor methods
def getName(self):
    return self.__name
def getAnimalType(self):
    return self.__animalType
def getAge(self):
    return self.__Age
#end method

def __str__(self):
    return self.__name + "is a" + self.__Age + "year old" + self.__animalType + "."


#call main
def main():
    print("This program tests the Pet Class.\n")
    
    myPet = Pet()
    myPet.setName(input("My Pet : "))
    myPet.setAnimalType(input("Pet type : "))
    myPet.setage(input("Pet age : "))

    print()
    print("Pet Name: ", myPet.getName())
    print("Pet Type: ", myPet.getAnimalType())
    print("Pet Age: ", myPet.getAge())
    print()
    print(myPet)

#end method
