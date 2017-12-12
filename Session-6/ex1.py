from turtle import *

def draw_multicolor_square(t, sz):
    for i in ['red', 'purple', 'hotpink', 'blue']:
        t.color(i)
        t.forward(sz)
        t.left(90)

tess = Turtle() # Creat tess
tess.pensize(3)

size = 20
for i in range(15):
    draw_multicolor_square(tess, size)
    size = size + 10 # increase the size for next time
    tess.forward(10) # Move Tess along a little
    tess.right(18) # give her some turn
