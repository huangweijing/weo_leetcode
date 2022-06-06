
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = int(dividend / divisor)
        if result < - 2 ** 31:
            result = -2 ** 31
        if result > 2 ** 31 - 1:
            result = 2 ** 31 - 1
        return result


sol = Solution()
r = sol.divide(999999999999999999999999999999999, -3)
print(r)
