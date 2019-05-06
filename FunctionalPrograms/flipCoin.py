import random
print("Enter the no of times to flip")
n = int(input())
head = 0
tail = 0
for i in range(n):
    flip = random.randint(0, 1)
    #if flip == 1:
        #head = head + 1
    #else:
        #tail = tail + 1
    if flip <= 0.5:
        tail = tail + 1
    else:
        head = head + 1
t = (tail * 100)/n
h = 100 - t
#print("Head Percentage:", head)
#print("Tail Percentage:", tail)
print("Head Percentage:", h)
print("Tail Percentage:", t)

