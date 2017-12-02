
while True:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Not a number! Try again!")
        continue
    else:
        break

found = False
if num > 1:
    for i in range(2, num-1):
        if num % i == 0:
            found = True
    if not found:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
else:
    print(num, "is not a prime number")

#num = 1 is explicitly wrong
