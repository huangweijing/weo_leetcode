import math
from functools import cache

class Solution:
    MODULO = 10 ** 9 + 7

    def __init__(self):
        self.x = 0
        self.max_exp = 0

    @cache
    def my_sol(self, n: int, from_int: int) -> int:
        max_exp = math.ceil(n ** (1 / self.x))
        ans = 0
        for i in range(from_int, max_exp):
            if n == i ** self.x:
                ans += 1
            else:
                ans += self.my_sol(n - i ** self.x, i + 1)
        print(f"n={n} x={self.x}, from_int={from_int}, ans={ans}, max_exp={max_exp}")
        return ans


    @cache
    def numberOfWays(self, n: int, x: int) -> int:
        self.x = x
        return self.my_sol(n, 0)
        # return ans % Solution.MODULO

data = [4, 1]
r = Solution().numberOfWays(*data)
print(r)