from random import *
words = ["champion", "environment", "hello", "beautiful", "software", "devlopment", "music", "indie"]
count = 0
while (count < 3):
    number = randint(0, len(words))
    guessword = words[number]
    words.remove(guessword)
    blah = list(guessword)
    print(guessword)
    shuffle(blah)
    print(*blah, sep=" ")

    answer = input("Your answer: ")
    if str(guessword) == answer:
        print("Huraa Correct!!")
    else:
        print("You stupid!")
    print()
    count += 1
