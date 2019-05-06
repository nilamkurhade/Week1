

from util.util_class import BubbleSort


try:
    """=======Integer array==="""
    arr = []
    #n = int(input("enter size of an array \n"))
    #print("enter array elements..\n")
    #for i in range(int(n)):
        #x = input()
        #arr.append(x)
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(BubbleSort(arr))

    """=======String array==="""
    my_list = []
    #print("enter array elements..\n")
    #for i in range(n):
        #y = input()
        #my_list.append(y)
    my_list = ['a', 'd', 'c', 'f', 'e']
    print(BubbleSort(my_list))

except RuntimeError:
    print("oops something went wrong....")
