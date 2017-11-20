import datetime
now = datetime.datetime.now()

# name = input("Hello! What's your name? ")
year = int(input("Tell me your year of birth? "))
age = now.year - year
print("Currently you are", age)
