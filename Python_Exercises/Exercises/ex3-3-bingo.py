# for x in range(10):
#     x_str = ''
#     x_str += str(x)
#     print("-")

#BINGO
#FINAL OUTPUT
import random
for j in range(2):
    num_str = "|"
    for i in range(1,6):
        rnd_number = random.randint(1, 99)
        num_str += str(rnd_number) + ' | '
    print(num_str)

# for i in range(1,6):
#     rnd_number = random.randint(1, 99)
#     num_str += str(rnd_number) + ' | '
# print(f"""-------------------------
# {num_str}
# {num_str1}
# -------------------------""")

