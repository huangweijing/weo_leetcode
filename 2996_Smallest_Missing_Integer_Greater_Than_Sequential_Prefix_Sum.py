from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        nums_set = set(nums)
        sum_seq = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                sum_seq += nums[i]
            else:
                break
        while sum_seq in nums_set:
            sum_seq += 1
        return sum_seq

