from util.util_class import vendingMachine


try:
    money = int(input("Enter the Money Values\n"))
    notes = [1000, 500, 100, 50, 20, 10, 5, 1]
    vendingMachine(money, notes)
except RuntimeError:
    print(" ")
