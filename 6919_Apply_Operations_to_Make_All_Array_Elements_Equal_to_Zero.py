from typing import List
from functools import cache


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        ope_arr = [0] * len(nums)
        ope = 0
        for i, num in enumerate(nums):
            # print(ope_arr, ope)
            ope += ope_arr[i]
            if ope + num < 0:
                return False
            else:
                diff = ope + num
                if diff > 0:
                    if i + k <= len(nums):
                        ope -= diff
                    else:
                        return False
                    if i + k < len(nums):
                        ope_arr[i + k] += diff
        return True


data = [
    [0,4,7,3]
    , 2
]
r = Solution().checkArray(* data)
print(r)
