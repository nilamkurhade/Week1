
from util.util_class import dayOfWeek

try:
    day = int(input("enter day"))
    month = int(input("enter Month"))
    year = int(input("enter year"))

    print(dayOfWeek(day, month, year))

except RuntimeError:
    print("oops something went wrong....")
