from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2 = nums.copy()
        nums2.sort()
        left, right = 0, len(nums) - 1
        has_not_equal = False
        for i in range(len(nums)):
            if nums[i] != nums2[i]:
                has_not_equal = True
                left = i
                break
        for i in reversed(range(len(nums))):
            if nums[i] != nums2[i]:
                has_not_equal = True
                right = i
                break
        if has_not_equal:
            return right - left + 1
        else:
            return 0