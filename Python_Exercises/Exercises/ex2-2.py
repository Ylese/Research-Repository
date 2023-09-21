# discount calculator
sum = input('Enter the total \033[91msum\033[0m of money spent: ')
sum = float(sum)
sum1 = sum*0.10
sum2 = sum*0.90
if sum >=500:
    print(f"Discount applied: \033[91m${sum1}\033[0m (10.0%)")
    print(f"Total to Pay after Discount: \033[91m${sum2}\033[0m")
