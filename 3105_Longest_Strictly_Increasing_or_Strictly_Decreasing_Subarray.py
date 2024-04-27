from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, dec = 1, 1
        max_inc, max_dec = 1, 1
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                dec += 1
                inc = 1
            elif nums[i - 1] < nums[i]:
                inc += 1
                dec = 1
            else:
                inc, dec = 1, 1
            max_inc = max(inc, max_inc)
            max_dec = max(dec, max_dec)
        return max(max_dec, max_inc)
