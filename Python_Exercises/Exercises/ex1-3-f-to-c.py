# To make this script more presentable, I used print function to print the title of this program first. I also included colors to make it more noticeable.
print("\033[91m|----Fareniheit to Celsius converter----|\033[0m")

# The standard data type in python is string, therefore, I used the function 'float()' to convert the string to a float data type. In that way, the user could only enter a float number(decimal numbers).
F = float(input("Enter temperature(Farenheit)"))

# I used 'x', 'y', and 'z' variables to input the numbers needed in the formula to convert Farenheit to Celsius. 
x = 32
y = 5
z = 9

# The variable 'result' contains the formula for Farenheit to Celsius
result = ((F - x) * y / z)

# The result will be printed, the temperature in Farenheit is now converted to Celsius.
print("Celsius =", result)