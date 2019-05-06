

from util.util_class import mergeSort


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")
    print(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    print(arr)
