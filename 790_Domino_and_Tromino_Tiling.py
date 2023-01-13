from functools import cache
import sys
sys.setrecursionlimit(20000)

class Solution:
    # Status
    # 0 1 2
    # x o x
    # x x o
    @cache
    def my_sol(self, n: int, shape: int) -> int:
        if n == 0:
            if shape == 0:
                return 1
            else:
                return 0
        if n == 1:
            return 1

        ans = 0
        if shape == 0:
            ans += self.my_sol(n - 2, 1)
            ans += self.my_sol(n - 2, 2)
            ans += self.my_sol(n - 1, 0)
            ans += self.my_sol(n - 2, 0)
        elif shape == 1:
            ans += self.my_sol(n - 1, 2)
            ans += self.my_sol(n - 1, 0)
        elif shape == 2:
            ans += self.my_sol(n - 1, 1)
            ans += self.my_sol(n - 1, 0)
        return ans % (10 ** 9 + 7)

    @cache
    def numTilings(self, n: int) -> int:
        return self.my_sol(n, 0)

r = Solution().numTilings(1000)
print(r)