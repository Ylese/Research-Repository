# Grade Calculator

# This line prompts the user to enter their exam mark as a string. The input function is used to collect the user's input, and it's stored in the variable mark.
mark = input("Enter your exam mark (0-100): ")

# This line converts the user's input (which is initially a string) into an integer. This step is necessary because you want to perform numerical comparisons later in the code.
mark = int(mark)

# The code uses a series of if, elif (short for "else if"), and else statements to determine the grade based on the user's exam mark.
if mark >= 90 and mark <=100:
    print("Your grade is \033[92mA+\033[0m") # checks if the mark falls between 90 and 100 (inclusive). If true, it prints "Your grade is A+."
elif mark >= 80 and mark < 90:
    print("Your grade is \033[92mA\033[0m") #checks if the mark falls between 80 and 89 (inclusive). If true, it prints "Your grade is A."
elif mark >= 70 and mark < 80:
    print("Your grade is \033[92mB\033[0m") # checks if the mark falls between 70 and 79 (inclusive). If true, it prints "Your grade is B."
elif mark >= 60 and mark < 70:
    print("Your grade is \033[92mC\033[0m") # checks if the mark falls between 60 and 69 (inclusive). If true, it prints "Your grade is C."
elif mark >= 50 and mark < 60:
    print("Your grade is \033[92mD\033[0m") # checks if the mark falls between 50 and 59 (inclusive). If true, it prints "Your grade is D."
elif mark < 50 and mark == 0:
    print("You \033[31mFailed\033[0m") # checks if the mark is less than 50 and greater than or equal to 0. If true, it prints "You Failed."

# 'else' is the default case. If none of the previous conditions are met, it prints "Incorrect input: the mark must be a number between 0 and 100 only." This is to handle cases where the user enters a mark outside the specified range or a non-numeric value.
else: 
    print("\033[31mIncorrect input: the mark must be a number between 0 and 100 only\033[0m")

