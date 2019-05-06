
from util.util_class import monthlyPayment


p = int(input("enter principale \n"))
y = int(input("enter year \n"))
r = float(input("enter rate of interest \n "))
print("mothly payment is ", monthlyPayment(p, y, r))
