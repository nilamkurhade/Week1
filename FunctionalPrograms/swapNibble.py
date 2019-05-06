
from util.util_class import toBinary


try:

    print("enter numbers \n")
    num = int(input())
    str1 = bin(num).replace("0b", "")
    print(str1)
    toBinary(str1)

except RuntimeError:
    print("oops something went wrong\n")
