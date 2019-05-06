import math

a = int(input("Enter number1:"))
b = int(input("Enter number2:"))
c = int(input("Enter number3:"))

r1 = 0.0
r2 = 0.0

delta = b * b - 4 * a * c

if delta > 0:
    r1 = (- b + math.sqrt(delta)) / (2 * a)
    r2 = (- b - math.sqrt(delta)) / (2 * a)

print("The roots of x are : " + str(r1) + " & " + str(r2))