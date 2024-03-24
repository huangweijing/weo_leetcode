from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        idx = None
        for i, num in enumerate(nums):
            if num == 0:
                continue
            if idx is None:
                idx = i
                continue
            if i - idx - 1 < k:
                return False
            idx = i
        return True

