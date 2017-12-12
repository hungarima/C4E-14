from random import *

def evaluate(x, y, op):
    if op == "+":
        a = x + y
    elif op == "-":
        a = x - y
    elif op == "*":
        a = x * y
    elif op == "/":
        a = round(x / y, 1)
    return a

# print(__name__)
