from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        idx = 0
        while True:
            if nums[idx] == target:
                return idx
            elif nums[idx] < target:
                left = idx
                idx = (idx + right) >> 1
            elif nums[idx] > target:
                right = idx
                idx = (idx + left) >> 1

            if idx + 1 < len(nums) and nums[idx] < target < nums[idx + 1]:
                return idx + 1
            if idx == len(nums) - 1 and nums[idx] < target:
                return idx + 1
            if idx == 0 and target < nums[idx]:
                return idx

sol = Solution()
r = sol.searchInsert([1,3,5,6], 7)
print(r)
r = sol.searchInsert([1,3,5,6], 2)
print(r)
r = sol.searchInsert([1,3,5,6], 5)
print(r)