from functools import cache

class Solution:
    @cache
    def count_num(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 9
        return self.count_num(n - 1) * (11 - n)

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        sum_val = 0
        for i in range(n + 1):
            sum_val += self.count_num(i)
        return sum_val

r = Solution().countNumbersWithUniqueDigits(3)
print(r)