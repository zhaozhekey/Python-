nums = [6, 5, 3, 1, 8, 7, 2, 4]

for i in range(0, len(nums)):
    for j in range(0, len(nums) - 1):
        if nums[j] > nums[j + 1]:
            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = temp
    print(nums)
print(nums)

# for n in range(0, len(nums) - 1):
#     if nums[n] > nums[n + 1]:
#         nums[n], nums[n + 1] = nums[n + 1], nums[n]
# print(nums)
