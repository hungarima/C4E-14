month1 = 1
x1 = 0
x2 = month1
for i in range(5):
    x3 = x1 + x2
    print("Month", i, ":", x3, "pair(s) of rabbit" )
    x1 = x2
    x2 = x3
