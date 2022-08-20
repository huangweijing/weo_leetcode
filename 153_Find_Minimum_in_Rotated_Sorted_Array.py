from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[1]
        if nums[0] < nums[-1]:
            return nums[0]

        low = 0
        high = len(nums) - 1
        mid = (low + high) >> 1

        while nums[mid] < nums[mid + 1]:
            if nums[0] <= nums[mid] < nums[mid + 1]:
                low = mid
            if nums[mid] < nums[mid + 1] <= nums[-1]:
                high = mid
            mid = (low + high) >> 1

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

        return nums[mid + 1]

data = [2, 1]
r = Solution().findMin(data)
print(r)

