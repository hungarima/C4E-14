# Sum of x and y

# x = int(input("x = "))
# y = int(input("y = "))
# sum = x + y
# print(x, "+", y, "=", sum)

x = int(input("x = "))
oper = input("Operation(+,-,*,/)")
y = int(input("y = "))

op = 0

if oper == "+":
    op = x + y
elif oper == "-":
    op = x - y
elif oper == "*":
    op = x * y
elif oper == "/":
    op = x / y


print(op)
