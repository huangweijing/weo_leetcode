from typing import List
import bisect


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        idx = len(nums) >> 1
        ans = 0
        for num in nums[: len(nums) >> 1]:
            while idx < len(nums) and num * 2 > nums[idx]:
                idx += 1
            if idx >= len(nums):
                break
            idx += 1
            ans += 2
        return ans

data = [1,78,27,48,14,86,79,68,77,20,57,21,18,67,5,51,70,85,47,56,22,79,41,8,39,81,59,74,14,45,49,15,10,28,16,77,22,65,8,36,79,94,44,80,72,8,96,78,39,92,69,55,9,44,26,76,40,77,16,69,40,64,12,48,66,7,59,10]
r = Solution().maxNumOfMarkedIndices(data)
print(r)