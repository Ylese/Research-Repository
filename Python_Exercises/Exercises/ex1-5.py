first_name = input("Enter your first name: ") # This line prompts the user to enter their first name and stores the input in the variable first_name.
family_name = input("Enter your last name: ") # This line prompts the user to enter their last name and stores the input in the variable family_name.
role = input("Enter your role: ") # This line prompts the user to enter their role and stores the input in the variable role.
result_string = first_name + " "+ family_name + " (" + role + ")" # This line constructs a result string by concatenating the first_name, a space, family_name, an open parenthesis, role, and a closing parenthesis. The + operator is used for string concatenation.
print("Result: \033[31m", result_string, "\033[0m") # This line prints the result string. 