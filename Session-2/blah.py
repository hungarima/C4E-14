m = 5
n = 6

for j in range(m):
    for i in range(n):
        if (i+j) % 2 == 0:
            print("*", end="")
        else:
            print("x", end="")
    print()
