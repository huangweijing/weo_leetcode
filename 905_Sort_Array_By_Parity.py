from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        back_idx = len(nums) - 1
        for i in range(len(nums)):
            if i >= back_idx:
                return nums
            while nums[i] & 1 == 1 and i < back_idx:
                nums[i], nums[back_idx] = nums[back_idx], nums[i]
                back_idx -= 1
        return nums

data = [1, 1, 1, 3, 7]
r = Solution().sortArrayByParity(data)
print(r)