import sys
import math

x1 = 0
y1 = 0
x2 = int(input("Enter value1"))
y2 = int(input("Enter value2"))

distance = int(math.sqrt((math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))))
#print("Euclidean Distance from point (0,0) to (" + x2 + "," + y2 + ") : ", distance)
print("distance", distance)
