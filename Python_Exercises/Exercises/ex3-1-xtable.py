# multiplication table

# This line prompts the user to enter a whole number, and the input is stored in the variable n. The int() function is used to convert the user's input (which is initially a string) into an integer.
n = int(input('Enter any whole number:'))

# This line sets up a for loop that iterates through the numbers from 1 to 20 (inclusive). The loop variable is i, which will take on values from 1 to 20 in each iteration.
for i in range(1,21):
    print(n,"x", i, "=", n*i) # This line calculates and prints the result of multiplying the user's input n by the loop variable i. It does this for each value of i from 1 to 20. The format of the print statement is designed to display the multiplication in the form of an equation, like "n x i = result."