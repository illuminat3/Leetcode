from StringToInteger import Solution

if __name__ == "__main__": 
    solution = Solution()
    print(solution.myAtoi("42"))
    print(solution.myAtoi("   -42"))
    print(solution.myAtoi("4193 with words"))
    print(solution.myAtoi("words and 987"))
    print(solution.myAtoi(".1"))
    print(solution.myAtoi("00000-42a1234"))
    print(solution.myAtoi("+0 123"))