from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(int(len(nums) / 2)):
            result = max(result, nums[i] + nums[len(nums) - 1 - i])
        return result