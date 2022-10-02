from functools import cache

class Solution:
    mod = 10 ** 9 + 7
    @cache
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n == 0 and target == 0:
            return 1
        if n == 0:
            return 0
        result = 0
        for i in range(1, k + 1):
            if target - i >= 0:
                result += self.numRollsToTarget(n - 1, k, target - i)
            result = result % Solution.mod
        return result

r = Solution().numRollsToTarget(2, 6, 7)
print(r)
