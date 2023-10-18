from typing import List
import math


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        stk = [nums[0]]
        if nums[1] > nums[0]:
            stk = [nums[1]]
            ij_max = 0
        else:
            stk.append(nums[1])
            ij_max = nums[0] - nums[1]
        ans = 0
        for i in range(2, len(nums)):
            # print(stk, nums[i])
            ans = max(ij_max * nums[i], ans)
            while len(stk) > 0 and stk[-1] < nums[i]:
                stk.pop()
            stk.append(nums[i])
            if len(stk) >= 2:
                ij_max = max(ij_max, stk[0] - stk[-1])
        return ans