from turtle import *

speed(-1)
begin_fill()
color("green", "yellow")
# Draw a square
for x in range(4):
  forward(100)
  left(90)

# Draw a triangle
for x in range(3):
  forward(100)
  left(120)

# Draw a Circle
circle(100)





end_fill()

# Multi-circles
for x in range(6):
  circle(-100)
  left(60)

# BETTERR
for x in range(8):
  for x in range(6):
      circle(-100)
      left(60)
  left(7)

mainloop()
