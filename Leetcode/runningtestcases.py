class TestCaseImplementation:
    def implement_test_cases(self, test_cases, function):
        for i in test_cases:
            print("Current test case: ", i)
            print("Output: ", function(i))
            print("")