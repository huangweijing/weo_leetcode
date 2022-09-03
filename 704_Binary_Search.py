from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if nums[0] > target:
            return -1
        if nums[-1] < target:
            return -1

        l, h = 0, len(nums)
        mid = (l + h) >> 1
        while l < h:
            if nums[mid] == target:
                return mid
            elif mid + 1 < len(nums) and nums[mid] < target < nums[mid + 1]:
                return -1

            if target > nums[mid]:
                l = mid
            if target < nums[mid]:
                h = mid
            mid = (l + h) >> 1

        return -1
