import math
from functools import cache

good_num = set[int]([2, 5, 6, 9])
valid_num = set[int]([0, 1, 8])

class Solution:
    def my_sol(self, n: int) -> list[int]:
        # if n == 0:
        #     return [0, 1]
        if n < 10:
            ret = [0, 0]
            for i in range(0, n + 1):
                if i in good_num:
                    ret[0] += 1
                elif i in valid_num:
                    ret[1] += 1
            return ret
        ten_base = 10 ** int(math.log10(n))
        if ten_base == n:
            ret = self.my_sol(n - 1)
            ret[1] += 1
        else:
            ret = [0, 0]
            ret_digit = self.my_sol(n // ten_base - 1)
            ret_tenbase = self.my_sol(ten_base - 1)
            # print(n // ten_base - 1, ret_digit, ten_base - 1, ret_tenbase)
            ret[1] += ret_digit[1] * ret_tenbase[1]
            ret[0] += sum(ret_digit) * sum(ret_tenbase) - ret[1]
            ret_remain = self.my_sol(n % ten_base)
            if n // ten_base in good_num:
                ret[0] += sum(ret_remain)
            elif n // ten_base in valid_num:
                ret[0] += ret_remain[0]
                ret[1] += ret_remain[1]
        # print(ret)
        return ret


    def rotatedDigits(self, n: int) -> int:
        ret = self.my_sol(n)
        # print(ret)
        return ret[0]

r = Solution().rotatedDigits(9999)
print(r)