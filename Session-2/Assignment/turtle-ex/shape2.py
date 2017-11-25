from turtle import *

# shape = int(input("Enter the number of polygon you want to draw: "))
# In this case:
shape = 4
for n in range(3, shape+3):
    if n % 2 == 0:
        color("red")
    else:
        color("blue")
    for u in range(n):
        forward(50)
        left(180-(((n-2)*180)/n))


# for i in range(3):
#     forward(50)
#     left(120)
# for i in range(4):
#     forward(50)
#     left(90)
# for i in range(5):
#     forward(50)
#     left(72)
# for i in range(6):
#     forward(50)
#     left(60)
mainloop()
