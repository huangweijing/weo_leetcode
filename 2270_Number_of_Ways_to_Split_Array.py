from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = 0
        sum_nums = sum(nums)
        left_sum = 0
        for i in range(len(nums) - 1):
            num = nums[i]
            left_sum += num
            sum_nums -= num
            if left_sum >= sum_nums:
                ans += 1
        return ans

