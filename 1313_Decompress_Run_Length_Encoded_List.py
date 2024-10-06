from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        idx = 0
        while idx < len(nums):
            n1 = nums[idx]
            n2 = nums[idx + 1]
            idx += 2
            ans.extend([n2] * n1)
        return ans

