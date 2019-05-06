# print all permutation with all duplicate.

def toString(list):
    return (''.join(list))


# function take three parameters string, starting index of string and last index of string
def permutation(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permutation(a, l + 1, r)
            a[l], a[i] = a[i], a[l]

# Driver program to test the above function
str1 = input("Enter the string:")
n = len(str1)
a = list(str1)
permutation(a, 0, n)