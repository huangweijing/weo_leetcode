from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        num = 0
        if num > nums[-1]:
            return 0
        for i in range(1, len(nums)):
            if nums[-i] >= i > nums[-(i + 1)]:
                return i
        if len(nums) <= nums[0]:
            return len(nums)
        return -1

data = [3,5]
r = Solution().specialArray(data)
print(r)