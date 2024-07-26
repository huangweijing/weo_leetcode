from typing import List
import bisect


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        pre_sum_arr = [0]
        for num in nums:
            pre_sum_arr.append(pre_sum_arr[-1] + num)
        for i, num in enumerate(nums):
            bisect.bisect_right(num + valueDiff
        