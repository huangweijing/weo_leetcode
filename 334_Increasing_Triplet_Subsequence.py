from typing import List
import math

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        stk = []
        min_order = math.inf
        for num in nums:
            while len(stk) > 0 and num <= stk[-1]:
                stk.pop()
            stk.append(num)
            if len(stk) >= 2:
                min_order = min(min_order, num)
            if min_order != math.inf and num > min_order:
                return True
        return False

data_nums = [20,100,10,12,5,11]
r = Solution().increasingTriplet(data_nums)
print(r)