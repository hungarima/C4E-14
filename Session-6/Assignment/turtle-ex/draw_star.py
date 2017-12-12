from turtle import *
pensize(2)
def draw_star(x, y, length):
    penup()
    setposition(x, y)
    pendown()
    for i in range(5):
        forward(length)
        right(144)
