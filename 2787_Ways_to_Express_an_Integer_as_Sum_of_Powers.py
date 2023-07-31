import datetime
import math
from functools import cache

class Solution:
    MODULO = 1000000007

    def __init__(self):
        self.x = 0
        self.max_exp = 0

    @cache
    def my_sol_with1(self, n: int, from_int: int) -> int:
        if n == 0:
            return 1
        if from_int * 2 > n:
            return 1
        res = 1
        for i in range(from_int, n + 1):
            next_n = n - i
            if next_n < i + 1:
                break
            sub_sol = self.my_sol_with1(next_n, i + 1)
            # if n - i ** self.x < i + 1 and sub_sol != 0:
            # print(f"my_sol({n - i ** self.x}, {i + 1})={sub_sol}")
            res += sub_sol
        # print("")
        return res % Solution.MODULO

    @cache
    def my_sol(self, n: int, from_int: int) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n == from_int ** self.x:
            return 1
        res = 0

        exp = n ** (1 / self.x)
        # print(abs(exp - math.ceil(exp)))
        if abs(exp - math.ceil(exp)) < 0.00000000001:
            if exp >= from_int:
                res = 1
        for i in range(from_int, n + 1):
            next_n = n - i ** self.x
            if next_n < i + 1:
                break
            sub_sol = self.my_sol(next_n, i + 1)
            # if n - i ** self.x < i + 1 and sub_sol != 0:
            # print(f"my_sol({n - i ** self.x}, {i + 1})={sub_sol}")
            res += sub_sol
        # print("")
        return res % Solution.MODULO

    # @cache
    def numberOfWays(self, n: int, x: int) -> int:
        self.x = x
        if self.x == 1:
            ans = self.my_sol_with1(n, 1)
        else:
            ans = self.my_sol(n, 1)
        # ans = self.my_sol(n, 1)
        return ans % Solution.MODULO

# start = datetime.datetime.now()
# data = [500, 1]
# r = Solution().numberOfWays(*data)
# end = datetime.datetime.now()
# print(r, end - start)

# dp = [1] + [0, 2]
# print(dp)