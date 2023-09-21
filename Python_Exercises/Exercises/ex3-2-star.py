# trial_1
# for x in range(1):
#     num_str = ''
#     for i in("*"):
#         num_str += str(i) + " "
#     for x in("*********"):
#         print(num_str)
#         num_str += str(i) + " "

# for i in range(11, 1, -1):
#     num_str = ''
#     for x in range(0, i-1):
#         num_str += str(i) + " "
#         print("*", end="")
#     print('\n')


# for i in range(11,1,-1):
#     for star in range(0, i-1):
#         print("*", end="")
#     print("\n")

# trial_2
# for x in range(1):
#     num_str = ''
#     for i in("*"+"*"+"*"+"*"+"*"+"*"+"*"+"***"):
#         num_str += str(i) + " "
#         print(num_str)

# FINAL OUTPUT
# STAR
    
for x in range(10): # This outer loop runs from 0 to 9 (10 times).
    num_str = '' # This initializes an empty string num_str for each iteration of the outer loop. This string will be used to build the pattern of asterisks.
    for i in range(1, x): # This inner loop runs from 1 to x - 1. In the first iteration of the outer loop (x = 0), this inner loop doesn't run because x - 1 is less than 1. In the subsequent iterations (x from 1 to 9), the inner loop will run, appending an asterisk followed by a space to num_str in each iteration.
        num_str += "* "
    print(num_str) # This line prints the accumulated num_str after the inner loop completes for each value of x. As x increases, the number of asterisks in num_str also increases
    
for x in range(10, 1, -1): # This outer loop runs from 10 down to 2, decreasing by 1 in each iteration.

    num_str = '' # This initializes an empty string num_str for each iteration of the outer loop.
    for i in range(1, x): # This inner loop runs from 1 to x - 1. In the first iteration of the outer loop (x = 10), this inner loop runs nine times, appending an asterisk followed by a space to num_str in each iteration. In subsequent iterations (x from 9 down to 2), the inner loop runs fewer times, resulting in fewer asterisks in num_str.
        num_str += "* "
    print(num_str) # This line prints the accumulated num_str after the inner loop completes for each value of x. As x decreases, the number of asterisks in num_str also decreases.
