from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = 0
        for i, num in enumerate(nums, start=1):
            if len(nums) % i == 0:
                ans += num ** 2
        return ans