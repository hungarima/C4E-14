numbers = [1, 6, 8, 1, 2, 1, 5, 6]
while True:
    try:
        num = int(input("Enter a number? "))
    except ValueError:
        print("not a number! Try again")
        continue
    else:
        break
    
count = 0
for i in range(0, len(numbers)):
    if num == numbers[i]:
        count+=1
if count == 1:
    print(num, "appears", count, "time in my list")
else:
    print(num, "appears", count, "times in my list")
