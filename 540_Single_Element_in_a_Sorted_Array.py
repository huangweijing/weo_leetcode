from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        left, right = 1, len(nums) - 2
        mid = len(nums) >> 1
        while left < right:
            if nums[mid - 1] != nums[mid] != nums[mid + 1]:
                return nums[mid]
            if mid & 1 == 0:
                if nums[mid] == nums[mid + 1]:
                    left = mid + 2
                else:
                    right = mid - 1
            elif mid & 1 == 1:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                    right = mid - 1
            mid = left + right >> 1
        return nums[mid]

nums = [1,1,2,2,3,3,4,4,5,5,7,8,8]
r = Solution().singleNonDuplicate(nums)
print(r)
