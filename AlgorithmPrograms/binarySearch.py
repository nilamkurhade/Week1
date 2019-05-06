
from util.util_class import binary_search


try:
    arr = list()
    n = int(input("enter a array size...\n"))
    print("enter array element...\n")
    for i in range(n):
        x = input()
        arr.append(x)
    key = input("enter key to search element in given array..\n")
    if key in arr:
        print("key found at position..=> ", binary_search(arr, key))
    else:
        print("entered element not found sorry...\n")
        print("===========================")

        my_list = list()
        print("enter array element...\n")
    for i in range(n):
        x = input()
        my_list.append(x)
    key = str(input("enter key to search element in given array..\n"))
    if key in my_list:
        print("key found at position..=> ", binary_search(my_list, key))
    else:
        print("entered element not found sorry... \n")

except RuntimeError:
    print("oops something went wrong...")
