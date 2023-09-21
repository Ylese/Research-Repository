import statistics
list = [2.08, 3.04, 1.07, 2.45, 7.46, 0.73, 0.46, 4.57, 9.05,7.95]
print("List: ", list)

res = 1
for val in list:
    res = res*val
print("Result of multiplication = ", res)
 
sum = sum(list)
print("sum  =", sum)

avg = statistics.mean(list)
print("avg =", avg)

min = min(list)
print("min =", min)

max = max(list)
print("max =", max)