
# num = int(input("Enter a number: "))
#
# if num > 1:
#     for i in range(2, num):
#         if (num % i == 0):
#             print("It's not a prime number")
#             break
#     else:
#         print("It's a prime number")
# else:
#     print("It's not a prime number")

from turtle import *

width(10)

for i in range(100):
    if (i) % 6 <3 :
        color("blue")
    else:
        color("red")
    forward(5)
    penup()
    forward(5)
    pendown()

mainloop()
