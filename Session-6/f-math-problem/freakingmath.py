from random import *
from calc import evaluate
def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0, 10)
    y = randint(1, 10)
    op = choice(["+", "-", "*", "/"])
    error = randint(-1, 1)
    result = evaluate(x, y, op) + error
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    return user_choice == (result == evaluate(x, y, op)):
