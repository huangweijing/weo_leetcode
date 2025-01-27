from typing import List

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        for i, num1 in enumerate(nums):
            min_val, max_val = num1, num1
            for j in range(i, len(nums)):
                min_val = min(min_val, nums[j])
                max_val = max(max_val, nums[j])
                ans += max_val - min_val
        return ans
        