def twoSum(numbers, target):
    num_map = {}
    output = []
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in num_map:
            output.append([num_map[complement] + 1, i + 1])
        num_map[num] = i
    return output[0]

numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))