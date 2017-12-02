nums = [4, 10, 24, 45, 69, 89, 100]
x = int(input("Enter a number? "))
found = False
lo = 0
hi = len(nums)

while hi > lo:
    mid = (hi + lo) // 2
    num = nums[mid]
    if x == num:
        found = True
        break
        print("Found")
    elif x < num:
        hi = mid
        print("Left")
    else:
        lo = mid + 1
        print("Right")
if not found:
    print("Not found")
