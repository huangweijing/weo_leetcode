from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i, ans = 0, []
        while i < len(nums):
            if nums[i] != 0:
                if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                    ans.append(nums[i] * 2)
                    i += 1
                else:
                    ans.append(nums[i])
            i += 1
        ans.extend([0] * (len(nums) - len(ans)))
        return ans

