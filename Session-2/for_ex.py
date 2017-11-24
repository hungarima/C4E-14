from random import randint

mood = randint(0, 100)
if mood < 30:
    print("I'm feeling sad")
elif mood < 60:
    print("I'm OK")
else:
    print('''''')
