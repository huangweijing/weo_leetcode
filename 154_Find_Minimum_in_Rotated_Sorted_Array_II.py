from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, last_idx = 0, len(nums) - 1
        while nums[left] == nums[last_idx] and left < last_idx:
            last_idx -= 1
        right = last_idx
        if nums[left] < nums[right]:
            return nums[left]
        mid = left + right >> 1
        while left <= right:
            if nums[mid] <= nums[last_idx] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] <= nums[last_idx]:
                right = mid - 1
            elif nums[mid] > nums[last_idx]:
                left = mid + 1
            mid = left + right >> 1
        return nums[mid]

data = [2, 2, 2, 0, 2]
r = Solution().findMin(data)
print(r)