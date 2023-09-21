# import random

# cities = ["New York", "Los Angeles", 
#           "Chicago", "Houston", 
#           "Miami", "San Francisco", 
#           "Seattle", "Boston", 
#           "Atlanta", "Dallas"]
# print("My next trip is to", random.choice(cities))

from random import choice #specific, no need to put random/rand in the front
cities = ["New York", "Los Angeles", 
          "Chicago", "Houston", 
          "Miami", "San Francisco", 
          "Seattle", "Boston", 
          "Atlanta", "Dallas"]
print("My next trip is to", choice(cities))