for u in range(10):
    if u % 2 == 0:
        for i in range(10):
            if (i+1) % 2 == 0:
                print('*', end='')
            else:
                print("x", end='')
    else:
        for i in range(10):
            if (i+1) % 2 == 0:
                print('x', end='')
            else:
                print("*", end='')
    print()
