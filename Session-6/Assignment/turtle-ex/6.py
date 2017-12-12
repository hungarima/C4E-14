from draw_star import draw_star
from turtle import *

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

mainloop()

#use random.randint() statement to generate a random number from -300 to 300. First we need to import random library then declare statement, assign number to a variable
