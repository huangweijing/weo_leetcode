from typing import List


class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        ans = 1 if nums[0] > 0 else 0
        for i, num in enumerate(nums):
            if i + 1 > num:
                if i + 1 == len(nums) or nums[i + 1] > i + 1:
                    ans += 1
        return ans
