from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i, num in enumerate(nums):
            if num ^ (ans & 1) == 0:
                ans += 1
        return ans
