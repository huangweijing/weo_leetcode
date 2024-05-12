class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while num1 > 0 and num2 > 0:
            if num1 > num2:
                ans += num1 // num2
                num1 %= num2
            elif num2 > num1:
                ans += num2 // num1
                num2 %= num1
            else:
                ans += 1
                break
        return ans
