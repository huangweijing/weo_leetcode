from typing import List
from functools import cache


class Solution:

    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return f"{nums[0]}/{nums[1]}"
        return str(nums[0]) + "/(" + "/".join(map(str, nums[1: ])) + ")"

