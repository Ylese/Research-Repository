#timer
#countdown the timer
# import time

import random # This line imports the random module, which provides functions for working with random numbers.

# counter = 5

# while counter >= 0:
#     time.sleep(1)
#     print(counter)
#     counter -= 1 #if we hide this, it will go infinite

#timer

# sec = 0
# while True: #it is infinite because it is true
#     time.sleep(1) #if this is hidden, it will go faster
#     print(sec)
#     sec+=1

#FOR

# for i in range(5, 0, -1):
#     print(i)

# for i in range(1, 11):
#     print(i)

#FOR
# num_str = ''
# for i in range(1,11):
#     num_str += str(i) + " "
# print(num_str)

# double loop
# for j in range(10):
#     num_str = ''
#     for i in range(1,11):
#         num_str += str(i) + " "
#     print(num_str)

#Random
num_str = "" # generate random numbers between 1 and 99 and concatenate them into the num_str
for i in range(1,11):
    rnd_number = (1, 99)
    num_str += str(rnd_number) + '|'
print(num_str)


