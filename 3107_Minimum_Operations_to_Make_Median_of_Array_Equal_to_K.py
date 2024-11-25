from typing import List


class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        idx = len(nums) // 2
        ans = 0
        if nums[idx] == k:
            return 0
        elif nums[idx] < k:
            while idx < len(nums) and nums[idx] < k:
                ans += k - nums[idx]
                idx += 1
        elif nums[idx] > k:
            while idx >= 0 and nums[idx] > k:
                ans += nums[idx] - k
                idx -= 1
        return ans
        