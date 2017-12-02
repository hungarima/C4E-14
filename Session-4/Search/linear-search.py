listnumber = [65, 23, 28, 58, 85, 45, 83, 97, 1]
number = int(input("Enter a number: "))
found = False
found_index = -1

for index, num in enumerate(listnumber):
    if num == number:
            found_index = index
            found = True
            break

if not found:
    print("Not Found")
else:
    print("Found {0} at {1}".format(num, index))
