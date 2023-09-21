fruits = ["Apple", "Pineapple", "Orange", "Pea"] #contains four strings
print(fruits, type(fruits))
#  list is a complex data type

# temp_list =  [10.25, 5.36, 8.25, 10.2]
# int_list = [12, 5, 889, 15]
# mixed_list = ["marina", 10, True, 12.56]

# True is boolean

# index
print(fruits[0])
print(fruits[1])
fruits [3] = "Lime"
print(fruits)
# # always starts with 0, that's why this prints 0, cause apple is 0, pineapple is 1, orange is 2, pea is 3

#length of the list
print("length of the list", len(fruits))
print(fruits[len(fruits) - 1]) #if we want to print the last element

#add a new element to the list
fruits.append("Banana")
fruits.append("Lemon")
print(fruits)

#remove an element from the list
fruits.pop()
fruits.pop(0) #remove the first element - 0
print(fruits)

int_list = [543, 234, 657, 123, 876, 345, 789, 456, 890, 567, 987, 678, 876, 345, 678, 234, 901, 123, 456, 789, 345, 678, 987, 543, 210, 765, 432, 109, 876, 321, 654, 567, 890, 345, 678, 987, 210, 765, 432, 987, 543, 210, 789, 456, 123, 890, 567, 876, 345, 654, 789, 432, 109, 876, 890, 234, 987, 456, 123, 210, 567, 543, 678, 765, 321, 345, 890, 876, 432, 109, 987, 654, 210, 567, 543, 890, 456, 123, 876, 345, 678, 987, 789, 543, 234, 567, 432, 890, 210, 765, 456, 876, 109, 678, 321, 987, 234, 543, 456, 890, 678, 321, 765]

print(int_list)

#loop through list
for num in int_list:
    print(num)


# calculate the maximum 
maximum = 0;
for num in int_list:
    if maximum < num:
        maximum = num
print("max=", maximum)

max = max(int_list)
print(type(int_list))
print("max=", max)

# calculate the minimum
minimum = min(int_list)
print("min=", minimum)

# calculate the average
import statistics
average = statistics.mean(int_list)
print("avg= ", average)

#  calculate the sum
sum = sum(int_list)
print("sum=", sum)