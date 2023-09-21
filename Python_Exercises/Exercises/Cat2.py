class Cat2:
    name: None
    age: None
    isHappy: None

    #constructor
    def __init__(self, name, age, isHappy = True):
        self.name = name
        self.age = age
        self.__isHappy = isHappy

    def sound(self):
        print("Meow!")

    def display(self):
        print('Cat')
        print('name:', self.name)
        print('age:', self.age)
        print('happy:', self.__isHappy)

        #abstraction is not an object, its a structure, a skeleton.

    #getter
    def get_isHappy(self):
        return self.__isHappy
    
    #setter
    def set_isHappy(self, new_happy):
        self.__isHappy = new_happy

# Inheritance
#child class
class DomesticCat(Cat2):
    owner: None

    def __init__(self, owner, name, age, isHappy = True):
        super().__init__(name, age, isHappy)
        self.owner = owner

#child class
class WildCat(Cat2):

    def sound(self):
        print("Hiss!")

#OOP
#abstraction
#encapsulation
#inheritance
#polymorphysm