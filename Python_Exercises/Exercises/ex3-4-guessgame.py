# GUESS GAME

# print("""*************************************
# \033[92mWelcome to the Guess the Number game!\033[0m
# *************************************""")

# print("I have chosen a number between \033[92m1\033[0m and \033[92m20\033[0m. Can you guess it?")
# input('Enter your guess (between 1 and 20): ')

# import random
# num = 20
# while num >= 1:
#     print(num)
#     num -= 1

import random
number = random.randint(1,20)
attempts = 0
game_over = False
print("\033[92mWelcome to the Guess the Number!\033[0m")
while game_over == False:
    guess = int(input("Enter your guess (between \033[92m1\033[0m and \033[92m20\033[0m): "))
    if guess > number:
        attempts += 1
        print("\033[91mToo high, guess again!\033[0m")
    elif guess < number:
        attempts += 1
        print("\033[91mToo low, guess again!\033[0m")
    else:
        if guess == number:
            game_over = True
            print(f"\033[92mCongratulations! You guessed the number {number} after {attempts} attempts\033[0m")