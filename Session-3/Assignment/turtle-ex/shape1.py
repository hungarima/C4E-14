from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

shapes = 5
for i in range(3, shapes + 3):
    color(colors[i-3])
    for u in range(i):
        forward(50)
        left(180 - ((i-2)*180)/i)

mainloop()
