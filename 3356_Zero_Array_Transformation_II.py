from typing import List
from collections import Counter
from functools import cache

class Solution:
    def __init__(self) -> None:
        self.nums = []
        self.queries = []

    @cache
    def my_sol(self, k: int) -> bool:
        ret = True
        inc_dec_dict = Counter()
        for i in range(k):
            query = self.queries[i]
            inc_dec_dict[query[0]] += query[2]
            inc_dec_dict[query[1] + 1] -= query[2]
        height = 0
        for i, num in enumerate(self.nums):
            if i in inc_dec_dict:
                height += inc_dec_dict[i]
            # print(height, num)
            if height < num:
                ret = False
                break
        # print(f"k={k}, inc_dec_dict={inc_dec_dict}, ret={ret}")
        return ret


    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if nums == [0] * len(nums):
            return 0
        self.nums, self.queries = nums, queries
        left, right = 0, len(queries)
        mid = left + right >> 1
        while left <= right:
            s1 = self.my_sol(mid - 1)
            s2 = self.my_sol(mid)
            if not s1 and s2:
                return mid
            elif s1 and s2:
                # print(f"mid={mid}")
                right = mid
            elif not s1 and not s2:
                left = mid + 1
            mid = left + right >> 1
            # print(f"left={left}, right={right}, mid={mid}")
            # print()
        return -1
    

data = [
[7,6,8]
, [[0,0,2],[0,1,5],[2,2,5],[0,2,4]]
]
r = Solution().minZeroArray(*data)
print(r)