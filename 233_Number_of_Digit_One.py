from functools import cache
import math


class Solution:
    @cache
    def countDigitOne(self, n: int) -> int:
        if n <= 1:
            return n
        hd = int(math.log10(n))
        hd_step = 10 ** hd
        ret = 0
        for i in range(0, n, hd_step):
            ret += self.countDigitOne(hd_step - 1)
            if i == 1:
                ret += hd_step
        ret += self.countDigitOne(n % hd_step)
        return ret

r = Solution().countDigitOne(9)
print(r)