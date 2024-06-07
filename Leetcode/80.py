def removeDuplicates(nums):
    if len(nums) <= 2:
        return nums

    index = 2  # start from the third element
    for i in range(2, len(nums)):
        if nums[i] != nums[index - 2]:
            nums[index] = nums[i]
            index += 1

    return nums[:index]

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(removeDuplicates(nums))  # Output should be [0, 0, 1, 1, 2, 3, 3]