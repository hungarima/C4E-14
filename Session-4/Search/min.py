from random import randint

nums = [randint(-100,100), randint(-100,100), randint(-100,100), randint(-100,100), randint(-100,100)]
print(nums)
minn = nums[0]
for num in nums:
    if minn > num:
          minn = num

print(minn)
