from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = -1
        for num in nums:
            if num > 0:
                if -num in nums_set:
                    ans = max(num, ans)
        return ans