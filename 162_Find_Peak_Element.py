import math
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-2] < nums[-1]:
            return len(nums) - 1

        l = 0
        h = len(nums)
        mid = (l + h) >> 1
        while l < h:
            if mid == 0:
                left = -math.inf
            else:
                left = nums[mid - 1]
            if mid == len(nums) - 1:
                right = -math.inf
            else:
                right = nums[mid + 1]

            if left < nums[mid] and nums[mid] > right:
                return mid
            elif left < nums[mid] < right:
                l = mid
            elif left > nums[mid] > right:
                h = mid
            else:
                l = mid
            mid = (l + h) >> 1

r = Solution().findPeakElement([1,2,9,2,7,1])
print(r)
