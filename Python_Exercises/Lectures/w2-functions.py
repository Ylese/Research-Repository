#circumference
#DRY, keeps repeating

# r1 = 2
# c1 = 2*3.14*r1
# print(c1)

# r2 = 10
# c2 = 2*3.14*r2
# print(c2)

# r3 = 100
# c3 = 2*3.14*r3
# print(c3)

#function calculates the circumference
#parameter: r - radius
import math #- it will import a large data in your program
# def is function

# from math import pi #import smth from the module, specific

def circumference(r):
    c = 2*r*math.pi
    return c

r1 = 2
c1 = 2*circumference(r1)
print(c1)

r2 = 10
c2 = 2*circumference(r2)
print(c2)

r3 = 100
c3 = 2*circumference(r3)
print(c3)

#parameters
def sum(a= 1, b = 0):
    return a + b
print(sum(1, 3))
print(sum(1))
print(sum())

#Visibility and lifetime
#def - define function

def Russia(name):
    message = "Welcome to Russia"
    if name !="":
        message += ", " + name
    message += "!"
    return message
print(Russia("Ying"))
# print(message) #error, since it is inside the function. inside the function stays inside the function, it'll only recognize the function/the defined function
