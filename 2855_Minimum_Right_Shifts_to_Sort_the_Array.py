from typing import List


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        found = False
        ans = -1
        if nums[-1] > nums[0]:
            ans = 0
            found = True
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if found:
                    return -1
                found = True
                ans = len(nums) - i
        if not found:
            return 0
        return ans


