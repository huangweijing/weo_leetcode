from typing import List


class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        idx = 1
        last_val = nums[0]
        ans = 0
        while idx < len(nums):
            jump = 1
            while idx < len(nums) - 1 and last_val > nums[idx]:
                jump += 1
                idx += 1
            ans += jump * last_val
            # print(f"jump={jump}, val={last_val}")
            # print(f", {nums[idx]}")
            if idx < len(nums):
                last_val = nums[idx]
                idx += 1
        return ans

data = [4,3,1,3,2]
r = Solution().findMaximumScore(data)
print(r)

