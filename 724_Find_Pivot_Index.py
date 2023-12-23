from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_right = sum(nums)
        sum_left = 0
        for i, num in enumerate(nums):
            sum_right -= num
            if sum_left == sum_right:
                return i
            sum_left += num
        return -1
