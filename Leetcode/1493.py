def longestSubarray(nums):
    if 0 not in nums:
        return len(nums) - 1

    max_length = 0
    left = 0
    zeros = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        max_length = max(max_length, right - left)

    return max_length

from Leetcode.runningtestcases import TestCaseImplementation

test_cases = [[0,0,1,1], [1,0,0,0,0], [1,1,0,0,1,1,1,0,1], [1,1,1], [0,1,1,1,0,1,1,0,1], [1,1,0,1]]
tester = TestCaseImplementation()
tester.implement_test_cases(test_cases, longestSubarray)