import random


print("How many coupons you want to generate")
coupan = int(input())
for x in range(coupan):
    print(random.randint(1, 101))

