from random import randint
sheepsize =[randint(0, 100), randint(0, 200), randint(0, 300), randint(0, 400), randint(0, 500), randint(0, 300), randint(0, 200)]
print("Hello, my name is Hung and these are my sheep size")
print(sheepsize)
blah = True
month = 0
while blah:

    next_month = input("Go to next month?(Y, N) or want to sell all of you sheep (S)")
    print()
    print()


    #Go to next month
    if next_month.upper() == "Y":
        month+=1
        print("Month", month)
        print("One month has passed, now here is my flock")
        sheepsize += [size + 50 for size in sheepsize]
        #This is just one way to handle the problem, TODO: Find another way
        for i in range(7):
            sheepsize.pop(i)
        print(sheepsize)
        print("Now my biggest sheep has size ", max(sheepsize), "let's shear it")
        print("After shearing, here is my flock")
        sheepsize[sheepsize.index(max(sheepsize))] = 8
        print(sheepsize)

    #Get rid of program
    elif next_month.upper() == "N":
        blah = False

    #Caculate the money of the sheep
    elif next_month.upper() == "S":
        total = sum(sheepsize)
        print("My flock has size in total:", total)
        print("I would get ", total, "* 2$ = ", total*2, "$")
        blah = False
    else:
        print("Wrong command! Try again")
