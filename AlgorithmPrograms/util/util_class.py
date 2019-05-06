import math


def BubbleSort(arr):

    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

################################################################################################


def insertionSort(arr):
    temp=0
    for i in range(len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and arr[j-1] > temp:
            arr[j] = arr[j-1]
            j = j-1
        arr[j] = temp
    return arr


##################################################################################################


def dayOfWeek(days, month, year):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'Jule', 'August', 'September', 'October', 'November', 'December']
    y0 = year - (14 - month) / 12
    x = y0 + y0 / 4 - y0 / 100 + y0 / 400
    m0 = month + 12 * ((14 - month) / 12) - 2
    d0 = (days + x + 31 * m0 / 12) % 7
    for i in range(len(days)):
        if i == d0:
            print("Day of this Date", days, "/", month, "/", year, ":", days[i])
    for i in range(len(month)):
        if i == (month-1):
            print("Month of this Date", days, "/", month, "/", year+" : ", month[i])


#######################################################################################################


def vendingMachine(money, notes):
    rem =0
    for i in range(0, len(notes), 1):
        if money >= notes[i]:
            callnotes = money // notes[i]
            rem = money % notes[i]
            money = rem
            total = int(callnotes)
            print(notes[i], "Notes :", callnotes)
    vendingMachine(money,notes)
    print("Total notes in Vending machine are:", total)


############################################################################################################


def binaryIntegerSearch(arr, l, r, x):
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

            # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binaryIntegerSearch(arr, l, mid - 1, x)

            # Else the element can only be present
        # in right subarray
        else:
            return binaryIntegerSearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


##############################################################################################################


def decimalToBinary(num):
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end=' ')


##############################################################################################################

def FahrenheitToCelsius(temp):
    ctemp = (temp - 32) * 5 / 9
    return ctemp


def CelsiusToFahrenheit(temp):
    ftemp = (temp * 9 / 5) + 32
    return ftemp


#############################################################################################################


def monthlyPayment(P, Y, R):
    n = 12 * Y
    r = R / (12 * 100)
    payment = (P * r) / 1 - (1 + r) * math.pow((1 + r), (-n))
    return payment


############################################################################################################


def sqrt(n): # taking input int n from user
    temp = n
    epilson = 1e-15
    while math.fabs(temp - n / temp) > epilson * temp: # fabs will give the absolute value
        temp = ((n / temp) + temp) / 2
    print("square root of ", n, "is:", temp) # prints the square root of n


##############################################################################################################


def prime(num):

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
            else:
                print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


##############################################################################################################


def binary_search(arr, key):

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

    if key == arr[mid]:
        return mid
    elif key < arr[mid]:
        end = mid - 1
    else:
        start = mid + 1

    return -1


###############################################################################################################


def toBinary(str1):
    while len(str1) != 8:
        str1 = "0" + str1
    print("binary number after padding:", str1)
    mid = len(str1) / 2
    part1 = str1[:int(mid)]
    part2 = str1[int(mid):]
    print("part1:", part1)
    print("part2:", part2)
    new_str = part2 + part1
    print("after padding:", new_str)
    new_no = int((new_str), 2)
    print("new number is", new_no)
    if isPowerOfTwo(new_no):
        print("yes,it is power of two\n")
    else:
        print("no,it is not power of 2 \n")


##############################################################################################################

def isPowerOfTwo(new_no):
    return math.ceil(log(new_no)) == math.ceil(log(new_no))


def log(x):
    return math.log10(x) / math.log10(2)


#############################################################################################################


def isAnagram(str1, str2):
    sort1 = sorted(str1)
    sort2 = sorted(str2)
    if sort1 == sort2:
        print("Given Strings are anagram")
    else:
        print("Given strings are not anagram")


##############################################################################################################


def primeNoInRange(lower, upper):
    for num in range(0, 1000 + 1):

        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
        else:
            print(num)

################################################################################################################


def isPrime():
    lower = 0
    upper = 1000
    for i in range(lower, upper):
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
        if flag == 0:
            print(i, "\t")

#################################################################################################################


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
