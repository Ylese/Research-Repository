# choice = input("Enter any string or number: ")
# choice_1 = input("Enter any string or number: ")
# choice_2 = input("Enter any string or number: ")
# choice_3 = input("Enter any string or number: ")
# choice_4 = input("Enter any string or number: ")
# mixed_list = [(choice),(choice_1), (choice_2), (choice_3), (choice_4)]
# print("My list: ", mixed_list)

# choices = input("Enter any string or number: ")
# for i in choice:
#     if x == ""
#     print(i)

user_inputs = []  # Initialize an empty list to store user inputs.

for x in range(5):
    mixed_list = ''  # Initialize an empty string for each iteration of the outer loop.
    for i in range(1, x + 1):  # Start from 1 and include x in the range.
        user_input = input('Enter any string or number: ')
        mixed_list += user_input
        user_inputs.append(user_input)  # Append the user input to the list.

# Print the list of user inputs.
print("User inputs: ", user_inputs)

