from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        pos = 0
        ans = 0
        for num in nums:
            pos += num
            ans += 1 if pos == 0 else 0
        return ans
