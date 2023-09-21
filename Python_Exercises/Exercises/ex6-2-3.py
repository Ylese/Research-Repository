# Importing modules
import string
import random 

# Set of possible characters 
char = string.ascii_letters + string.punctuation + string.digits

# Creating password of random size and displaying it
password =  "".join(random.choice(char) for i in range(10))
print(f"New password is:", (password))