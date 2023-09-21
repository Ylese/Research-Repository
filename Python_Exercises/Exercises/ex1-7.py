print("n + nn + nnn")
n = input('Enter any digit: ') # prints the string "n + nn + nnn" as a header and allows the user to input a single digit

n = int(n)

nn = n * 11 # multiplies the value of n by 11
nnn = n * 111 # multiplies the value of n by 111

result = n + nn + nnn
# print("n + nn + nnn =", result) # calculates the sum of n, nn, and nnn
print(f"{n} + {nn} + {nnn} = {result}") # f-string (formatted string literal) to print the values of n, nn, and nnn, along with the calculated result
