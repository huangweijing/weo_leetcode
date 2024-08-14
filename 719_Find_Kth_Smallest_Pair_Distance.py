from typing import List
import bisect
from functools import cache


class Solution:
    def __init__(self) -> None:
        self.nums = []

    @cache
    def pair_cnt_le(self, dist: int) -> int:
        ret = 0
        for i, num in enumerate(self.nums):
            cnt = bisect.bisect_right(self.nums, num + dist) - (i + 1)
            ret += cnt
        return ret

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        self.nums = nums
        left, right = 0, nums[-1] - nums[0]
        mid = (left + right) >> 1
        while left < right:
            s1 = self.pair_cnt_le(mid - 1)
            s2 = self.pair_cnt_le(mid)
            if s1 < k <= s2:
                return mid
            elif k <= s1:
                right = mid - 1
            elif k > s2:
                left = mid + 1
            mid = (left + right) >> 1
        return mid


data = [
    [1, 4, 6, 7, 10, 15]
    , 7
]
s = Solution()
r = s.smallestDistancePair(*data)
# print(s.pair_cnt_le(2))
print(r)