from turtle import *

def draw_square(length, color):
    pencolor(color)
    for i in range(4):
        forward(length)
        right(90)
