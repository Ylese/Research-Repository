# To start this program...
# The user must input a specific programming language
language = input("Enter the programming language: ")

# once the user has entered their chosen programming language, using if-else statement, the program will print the corresponding job that aligns with the chosen program.
if language == "JavaScript":
    print("You can become a web developer")
elif language == "PHP":
    print("You can become a Backend Developer")
elif language == "Python":
    print("You can become a Data Scientist")
elif language == "Solidity":
    print("You can become a Blockchain Developer")
elif language == "Java":
    print("You can become a Mobile App Developer")
else:
    print("The language doesn't matter, what matters is solving problems.")