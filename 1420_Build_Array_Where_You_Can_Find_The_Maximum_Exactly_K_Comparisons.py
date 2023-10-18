import math
from functools import cache


class Solution:
    MOD = 10 ** 9 + 7
    def __init__(self):
        self.k = 0
        self.m = 0
        self.n = 0

    @cache
    def my_sol(self, idx: int, cur_max: int, k: int) -> int:
        if k < 0:
            return 0
        if idx == self.n:
            if k == 0:
                return 1
            else:
                return 0
        ans = 0
        if cur_max > 0:
            ans += self.my_sol(idx + 1, cur_max, k) * cur_max % Solution.MOD
        for next_cur_max in range(cur_max + 1, self.m + 1):
            ans += self.my_sol(idx + 1, next_cur_max, k - 1)
        return ans % Solution.MOD

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        self.n, self.m, self.k = n, m, k
        return self.my_sol(0, 0, k)

data = [
10
, 3
, 2
]
r = Solution().numOfArrays(* data)
print(r)

import math
print(math.comb(100, 50))