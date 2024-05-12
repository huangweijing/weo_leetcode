from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        val = 0
        for i, num in enumerate(nums):
            if val > num and nums[i - 1] <= val == i:
                return val
            val += 1
        if val == len(nums):
            return val
        return -1

data = [0, 0]
r = Solution().specialArray(data)
print(r)