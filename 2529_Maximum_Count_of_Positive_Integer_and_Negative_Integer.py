from typing import List
import bisect


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg_to = bisect.bisect_left(nums, 0)
        pos_from = bisect.bisect_right(nums, 0)
        return max(neg_to + 1, len(nums) - pos_from)
