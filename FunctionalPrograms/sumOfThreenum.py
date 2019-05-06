n = [2, 2, -3, 3, -4]

for i in range(len(n)):
    for j in range(i + 1, len(n)):
        for k in range(j + 1, len(n)):
            if (n[i] + n[j] + n[k]) == 0:
                print("Sum of triplet is  =", 0)