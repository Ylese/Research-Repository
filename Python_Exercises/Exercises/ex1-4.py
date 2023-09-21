# x = 100
# y = 5 
# z = 10

# x = int(input("Enter value (x)= "))
# y = int(input("Enter value (y)= "))
# z = int(input("Enter value (z)= "))

#   converts to float
x = float(input("Enter value (x)= "))
y = float(input("Enter value (y)= "))
z = float(input("Enter value (z)= "))

result = x + (1 + x**2 / y**2)**z - (x*y*z) # calculates the value of result 
print("Enter numeric values: ")
print()
print ("result = ", result)