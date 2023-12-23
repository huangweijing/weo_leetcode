from typing import List
from sortedcontainers import SortedList


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        ans = 0
        sl = SortedList()
        for i in range(len(nums1)):
            d = nums1[i] - nums2[i]
            idx = sl.bisect_right(d + diff) - 1
            if idx != -1:
                ans += idx + 1
            sl.add(d)
        return ans
