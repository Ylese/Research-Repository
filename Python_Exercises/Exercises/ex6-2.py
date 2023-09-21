import string
import random

char_alpha =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
char_punctuation = ["!","@","#","$","%","^","&","*","(",")","_","+","=","-","/",">","<",",",".","?","\\"]
char_digits = ["0","1","2","3","4","5","6","7","8","9"]

options = [char_alpha, char_punctuation, char_digits]
for i in range(10):
    choice = random.choice(options)
    digit = random.choice(choice)
    print(digit, end = '')


# num_str = ""
# for i in range(1,11):
#     rnd_number = (1, 99)
#     num_str += str(rnd_number) + '|'
# print(num_str)


