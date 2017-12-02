from random import randint

nums = [randint(-100,100), randint(-100,100), randint(-100,100), randint(-100,100), randint(-100,100), randint(-100,100), randint(-100,100), randint(-100,100), randint(-100,100), randint(-100,100)]
# print(nums)
# sum = 0
#
# for index, num in enumerate(nums):
#     sum += num
#
# print(sum)
sum = sum(nums)
print(sum)
