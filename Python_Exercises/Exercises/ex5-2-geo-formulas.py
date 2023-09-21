import math
#  Define a function for calculating the circumference of a circle
def circumference(r):
    c = 2*math.pi*r
    return c
# Calculate and print the circumference of a circle
r1 = 10
c1 = circumference(r1) 
print(c1)

# function for calculating the area of a circle
def circle_area(r):
    a = math.pi*r**2
    return a

r2 = 10
c2 = circle_area(r1)
print(c2)

# function for calculating the surface area of a sphere
def sphere_area(r):
    a1 = 4*math.pi*r**2
    return a1

r3 = 10
c3 = sphere_area(r3)
print(c3)

# function for calculating the volume of a sphere
def sphere_vol(r):
    v = 4/3*math.pi*r**3
    return v

r4 = 10
c4 = sphere_vol(r4)
print(c4)

#  function for calculating the perimeter of a rectangle
def rec_perimeter(p):
    w = 5
    h = 4
    p = 2*(w + h)
    return p

r5 = 10
c5 = rec_perimeter(r5)
print(c5)

#  function for calculating the area of a rectangle
def rec_area(length, height):
    area = height * length
    print(f"The area =", area)
rec_area(20, 100)