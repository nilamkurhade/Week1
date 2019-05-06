print("Enter year to be checked")
year = int(input())

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("given year is leap year")
else:
    print("Given year is not a leap year")

