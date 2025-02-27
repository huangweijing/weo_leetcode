from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        seq_size = 0
        for i, num in enumerate(nums):
            if i == 0 or num <= nums[i - 1]:
                seq_size = num
            elif num > nums[i - 1]:
                seq_size += num
            ans = max(ans, seq_size)
        return ans