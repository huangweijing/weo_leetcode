from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        sum_num = sum(nums)
        for num in nums:
            sum_num -= num
            if num < sum_num:
                return num + sum_num
        return -1
