from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        ans = 0
        last_ones = 0
        total_zeros = 0
        while i < len(nums):
            ones, zeros = 0, 0
            while i < len(nums) and nums[i] == 1:
                ones += 1
                i += 1
            while i < len(nums) and nums[i] == 0:
                zeros += 1
                i += 1
            total_zeros += zeros
            ans = max(ans, ones + last_ones)
            if zeros == 1:
                last_ones = ones
            else:
                last_ones = 0
        if total_zeros == 0:
            return ans - 1
        else:
            return ans

data = [
[1,1,1]
]
r = Solution().longestSubarray(* data)
print(r)