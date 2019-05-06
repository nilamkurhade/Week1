from util.util_class import insertionSort


try:
    """=======Integer array==="""
    arr = []
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(insertionSort(arr))

    """=======String array==="""
    my_list = []
    my_list = ['a', 'd', 'c', 'f', 'e']
    print(insertionSort(my_list))

except RuntimeError:
    print("oops something went wrong....")
