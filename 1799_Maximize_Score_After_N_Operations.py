from typing import List
from functools import cache
from collections import Counter
from sortedcontainers import SortedList


class Solution:
    def __init__(self):
        self.cache = dict[str, int]()
        self.nums_len = 0

    @cache
    def calc_gcd(self, n1: int, n2: int) -> int:
        if n2 != 0:
            return self.calc_gcd(n2, n1 % n2)
        else:
            return n1

    def my_sol(self, nums: SortedList, ith: int) -> int:
        key = ".".join(map(str, nums)) + "_" + str(ith)
        if key in self.cache:
            return self.cache[key]
        ans = 0
        nums_copy = nums.copy()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                nums_copy.remove(nums[i])
                nums_copy.remove(nums[j])
                val = self.calc_gcd(nums[i], nums[j]) * ith + self.my_sol(nums_copy, ith + 1)
                ans = max(ans, val)
                nums_copy.add(nums[i])
                nums_copy.add(nums[j])
        self.cache[key] = ans
        return ans

    def maxScore(self, nums: List[int]) -> int:
        self.nums_len = len(nums)
        return self.my_sol(SortedList(nums), 1)


data = [773274,313112,131789,222437,918065,49745,321270,74163,900218,80160,325440,961730]
# data = [1, 2, 3, 4, 5, 6, 7, 3, 2, 4, 9, 12, 14, 21]
# data = [1,2,3,4,5,6]
r = Solution().maxScore(data)
print(r)