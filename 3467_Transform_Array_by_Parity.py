from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        cnt0, cnt1 = 0, 0
        for num in nums:
            cnt0 += not (num & 1)
            cnt1 += num & 1
        return [0] * cnt0 + [1] * cnt1