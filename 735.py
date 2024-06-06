def asteroidCollision(asteroids):
    """
    :type asteroids: List[int]
    :rtype: List[int]
    """
    stack = []
    for asteroid in asteroids:
        while stack and asteroid < 0 < stack[-1]:
            if abs(asteroid) > stack[-1]:
                stack.pop()
                continue
            elif abs(asteroid) == stack[-1]:
                stack.pop()
            break
        else:
            stack.append(asteroid)
    return stack


from runningtestcases import TestCaseImplementation


test_cases = [[5,10,-5], [8,-8]]
tester = TestCaseImplementation()
tester.implement_test_cases(test_cases, asteroidCollision)

