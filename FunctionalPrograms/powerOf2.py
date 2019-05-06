print("Enter the number")
n = int(input())
if n>=32:
    print("Enter the power less than 32")
else:
    result = list(map(lambda x:2 ** x,range(n)))
for i in range(n):
    print("2^",i,"is",result[i])
