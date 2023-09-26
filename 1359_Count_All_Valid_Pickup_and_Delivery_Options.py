from functools import cache


class Solution:

    MOD = 10 ** 9 + 7

    def countOrders(self, n: int) -> int:
        ans = 1
        for i in range(n):
            space = i * 2 + 1
            val = (space * (space + 1)) // 2
            ans = (ans * val) % Solution.MOD
        return ans

r = Solution().countOrders(500)
print(r)