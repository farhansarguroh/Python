from Leetcode.runningtestcases import TestCaseImplementation

def removeStars(s):
    stack = []
    for i in s:
        if i == '*':
            stack.pop() if stack else None
        else:
            stack.append(i)
    return "".join(stack)

test_cases = ["leet**cod*e", "erase*****"]
tester = TestCaseImplementation()
tester.implement_test_cases(test_cases, removeStars)
