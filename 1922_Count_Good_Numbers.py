from functools import cache


mod = 10 ** 9 + 7
class Solution:
    @cache
    def my_sol(self, first: int, n: int) -> int:
        if n == 1:
            return first
        elif n == 2:
            return 20
        if n & 1 == 0:
            half = n // 2
            if half & 1 == 0:
                half_res = self.my_sol(first, half) % mod
                return (half_res * half_res) % mod
            else:
                half_res1 = self.my_sol(first, half) % mod
                half_res2 = self.my_sol(20 // first, half) % mod
                return (half_res1 * half_res2) % mod
        else:
            return (first * self.my_sol(first, n - 1)) % mod

    @cache
    def countGoodNumbers(self, n: int) -> int:
        return self.my_sol(5, n)
    
# print(Solution().countGoodNumbers(4))