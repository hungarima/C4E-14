shop = ['T-Shirt', 'Sweater']
action = ""
print("If you want to quit enter Q")
while ( not action.upper() == "Q" ):
    action = input("Welcome to our shop, what do you want (C, R, U, D, Q)? ")
    if action.upper() == "C":
        new = input("Enter new item: ")
        shop.append(new)
        print("Our items: ", end="")
        print(*shop, sep=", ")
    elif action.upper() == "R":
        print("Our items: ", end="")
        print(*shop, sep=", ")
    elif action.upper() == "U":
        upposition = int(input("Update position? "))
        upnew = input("New item? ")
        shop[upposition - 1] = upnew
        print("Our items: ", end="")
        print(*shop, sep=", ")
    elif action.upper() == "D":
        delposition = int(input("Delete position? "))
        shop.pop(delposition - 1)
        print("Our items: ", end="")
        print(*shop, sep=", ")
    elif action.upper() == "Q":
        action.upper() == "Q"
    else:
        print("Wrong Order!! Try again")

# print("Our items: ", end="")
# print(*shop, sep=", ")
