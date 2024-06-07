def maxProfit(prices):
    
    if not prices or len(prices)<2:
        return 0

    profit_earned = 0
    buy = prices[0]
    for price in prices[1:]:
        if price < buy:
            buy = price
        elif price > buy:
            profit_earned += (price - buy)
            buy = price
    
    return profit_earned
        
        
from Leetcode.runningtestcases import TestCaseImplementation


test_cases = [[7,1,5,3,6,4], [1,2,3,4,5], [7,6,4,3,1], [2,4,1]]
tester = TestCaseImplementation()
tester.implement_test_cases(test_cases, maxProfit)

