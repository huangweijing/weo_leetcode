from functools import cache
import sys
sys.setrecursionlimit(10000)
class Solution:
    @cache
    def my_sol(self, a_vol: int, b_vol: int) -> float:
        if a_vol <= 0 and b_vol <= 0:
            return 0.5
        if a_vol <= 0:
            return 1
        if b_vol <= 0:
            return 0

        a_vol = 0 if a_vol < 0 else a_vol
        b_vol = 0 if b_vol < 0 else b_vol

        p1 = self.my_sol(a_vol - 100, b_vol) * 0.25
        p2 = self.my_sol(a_vol - 75, b_vol - 25) * 0.25
        p3 = self.my_sol(a_vol - 50, b_vol - 50) * 0.25
        p4 = self.my_sol(a_vol - 25, b_vol - 75) * 0.25
        # print(p1, p2, p3, p4)
        if abs(p1 + p2 + p3 + p4 - 1) < 0.000001:
            return 1
        return p1 + p2 + p3 + p4

    def soupServings(self, n: int) -> float:
        if n >= 10000:
            return 1
        for i in range(n):
            self.my_sol(n, n)
        return self.my_sol(n, n)

r = Solution().soupServings(10000000)
print(r)