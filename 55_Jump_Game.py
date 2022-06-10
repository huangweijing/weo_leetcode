from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_range = 0
        for idx, num in enumerate(nums):
            if idx > max_range:
                return False
            if max_range >= len(nums) - 1:
                return True
            if idx + num > max_range:
                max_range = idx + num


sol = Solution()
r = sol.canJump([3, 2, 1, 0, 0, 0])
print(r)
