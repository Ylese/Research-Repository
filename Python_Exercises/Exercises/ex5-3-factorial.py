import math
# n = int(input('Enter any whole number:'))
    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Enter any whole number: "))

print(factorial(n))
print(f"{n}! = {factorial(n)}")

