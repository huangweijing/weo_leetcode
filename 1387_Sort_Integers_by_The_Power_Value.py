from functools import cache

class Solution:
    @cache
    def power(self, num):
        if num == 1:
            return 0
        if num & 1 == 0:
            return self.power(num >> 1) + 1
        else:
            return self.power(num * 3 + 1) + 1

    def getKth(self, lo: int, hi: int, k: int) -> int:
        pow_list = list(zip(range(lo, hi + 1), map(self.power, range(lo, hi + 1))))
        pow_list.sort(key=lambda x: x[1])
        return pow_list[k - 1][0]

r = Solution().getKth(7, 11, 4)
print(r)
