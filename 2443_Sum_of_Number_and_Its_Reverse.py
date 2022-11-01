import math


class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        num_len = len(str(num))
        from_num = 10 ** (num_len - 1)
        to_num = (10 ** num_len) >> 1
        if num < 10 ** (num_len - 1) * 2:
            from_num = 10 ** (num_len - 1) >> 1
        for i in range(from_num, to_num):
            if num == i + int(str(i)[::-1]):
                return True
        return False

r = Solution().sumOfNumberAndReverse(63)
print(r)

