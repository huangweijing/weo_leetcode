from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        last = nums[0]
        for num in nums[1:]:
            if num & 1 == last & 1:
                return False
            last = num
        return True
