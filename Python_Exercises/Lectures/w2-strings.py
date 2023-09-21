#strings

my_string = "Hello, Students!"
print(type(my_string))

my_string = 'Hello, Students!'
print(type(my_string))

print(my_string[0]) #used in lists
print(my_string[1 : 5]) 

#string is a list of characters
for character in my_string:
    print(character)

print("The length of my string is ",len(my_string)) #length of the strings

print("A" < "a", ord('A'), ord('a')) #true, cause decimal and binary of capital A is less than lower case a #ord - that's how python identify the order

# comparison of the strings
print("cookie" < "Cookie")
print("00:15"<"12.45")

# concatination
str1 = "Chocolate"
str2 = "Muffin"
str3 = str1 + ' ' + str2 # '' is space
print(str3)

str4 = (str1 + " ") * 3 + str2
print(str4)

#convert
str5 = str(10.23) #convert the number into string
print(str5)

#empty string
empty_string = '' #or ""
print(empty_string)

#long string
print('''
0_0
      ''')

#\n is a new line

print("Hello, Students!")
print("Hello, \nStudents!")
print("Hello, \tStudents!") #\t is tab
