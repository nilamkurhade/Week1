
from util.util_class import binary_search


try:
    newfile = open("search.txt", "r+")
    readfile = newfile.read()
    regex = readfile
    my_list = []
    my_list = regex.lower().split()
    print("before sorting \n")
    print(my_list)
    res = my_list
    print("enter word to search \n")
    word = input()
    if word in res:
        print("word=>", word, "found at position=>", binary_search(my_list, word))
    else:
        print("element not found \n")

except IOError:
    print("oops something went wrong\n")