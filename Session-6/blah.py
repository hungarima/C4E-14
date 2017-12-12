from random import *
count = 0
score = 0
blah = True
while blah :
    x = randint(0,10)
    y = randint(1,10)

    oper_list = ["+", "-", "*", "/"]
    random_index = randrange(0, len(oper_list))
    oper = oper_list[random_index]

    if oper == "+":
        a = x + y
    elif oper == "-":
        a = x - y
    elif oper == "*":
        a = x * y
    elif oper == "/":
        a = round(x / y, 1)


    b = randrange(-1,2)
    c = a + b
    print (x , oper, y, "=", c)
    if b == 0:
        ans = input("Y/N? ").upper()
        if ans == "Y":
            print("Yay")
            score += 1
        else:
            print("Stupid!")
            blah = False
    else:
        ans = input("Y/N? ").upper()
        if ans == "N":
            print("Yay")
            score += 1
        else:
            print("Stupid!")
            blah = False
    print("*" * 20)
    # count +=1
print("Your score: ", score)
