import math


while True:
    try:
        b = int(input("How many B bacterias are there? "))
        t = int(input("How much time in minutes will we wait? "))
    except ValueError:
        print("Not a number! Try again!")
        continue
    else:
        break


total = b * 2 ** math.floor(t/2)
print("After", t, "minutes, we would have", total, "bacterias")
