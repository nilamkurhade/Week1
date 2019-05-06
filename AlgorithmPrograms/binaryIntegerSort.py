
from util.util_class import binaryIntegerSearch


try:
    arr = []
    arr = [10, 20, 30, 40, 20]
    x = 30

    result = binaryIntegerSearch(arr, 0, len(arr) - 1, x)

    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")
except RuntimeError:
    print(" ")

