from typing import List
from collections import Counter
from functools import cache

class Solution:
    def __init__(self):
        self.num_cnt = Counter()
        self.keys = []

    @cache
    def my_sol(self, n) -> int:
        if n < 0:
            return 0
        key = self.keys[n]
        if n == 0:
            return key * self.num_cnt[key]
        if key - 1 in self.num_cnt:
            ans = max(key * self.num_cnt[key] + self.my_sol(n - 2), self.my_sol(n - 1))
        else:
            ans = key * self.num_cnt[key] + self.my_sol(n - 1)
        return ans


    def deleteAndEarn(self, nums: List[int]) -> int:
        self.num_cnt = Counter(nums)
        self.keys = list(self.num_cnt.keys())
        self.keys.sort()
        return self.my_sol(len(self.keys) - 1)

data = [2,2,3,3,3,4]
r = Solution().deleteAndEarn(data)
print(r)