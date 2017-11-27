from random import randint

guessNumber = randint(0, 100) # Tính cả số 100
# print(guessNumber)

yourGuess = -1
#guess_wrong= True
while (guessNumber != yourGuess):#guesswrong #True
    yourGuess = int(input("Guess number from 0 to 100: "))
    if guessNumber < yourGuess:
        if (yourGuess - guessNumber) < 10:
            print("A little too big")
        else:
            print("Too big")
    elif guessNumber > yourGuess:
        if (guessNumber - yourGuess) < 10:
            print("A little too small")
        else:
            print("Too small")
    else:
        print("Bingoo!!")
        #guess_wrong = False
        #break


#nhập một số xong bắt máy đoán khi nào ra thì thôi hoặc là cho đoán 7 lần nếu không đúng thì thua
