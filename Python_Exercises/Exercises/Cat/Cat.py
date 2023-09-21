
## printing cats with different colors and sound (beep)

import winsound
from random import choice

class Cat():
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def display_data(self):
        print("Cat:", self.name)
        print("Age:", self.age)
        print("Color:", self.color)

    
    def display(self):
        if self.color == "Magenta":
            print("""\033[35m(\___/)
(=*.*=)  
U-----U\033[0m""" )
        elif self.color == "Green":
            print("""\033[32m(\___/)
(=*.*=)  
U-----U\033[0m""")
        elif self.color == "Blue":
            print("""\033[34m(\___/)
(=*.*=)  
U-----U\033[0m""")
    
    def sound(self):
        winsound.Beep(800, 500)
        print("Meow!")


cat = Cat("Chico", "1", "Green")
cat1 = Cat("Mochi", "2", "Blue")
cat.display_data()
cat.display()
cat.sound()
cat1.display_data()
cat1.display()
cat1.sound()