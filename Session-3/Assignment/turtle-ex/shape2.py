from turtle import *

colors= ['red', 'blue', 'brown', 'yellow', 'grey']
shapes = 5
for i in range(shapes):
    begin_fill()
    color(colors[i], colors[i])
    for u in range(2):
        forward(60)
        right(90)
        forward(90)
        right(90)
    forward(60)
    end_fill()


mainloop()
