
nums = [-12, 4, 6, 7, 1234, 345, 345, -4, 23424, 42424, -7, -1234]
found = False

# for i in range(len(nums)):
#     x1 = nums[i]
#     for u in range(i, len(nums)):
#         if x1 + nums[u] == 0:
#             found = True
#             print(x1, nums[u])
for j in range(0, len(nums) - 1):
    x1 = nums[j]
    x2 = 0
    found = False
    for i in range(j + 1, len(nums)):
        if x1 + nums[i] == 0:
            x2 = nums[i]
            found = True
            break
    if found:
        print("Found {0} and {1}". format(x1, x2))
