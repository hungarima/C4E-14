from turtle import *

def draw_square(t, sz):
    """Make turtle t draw a square of sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)

alex = Turtle()
draw_square(alex, 50)

mainloop()
