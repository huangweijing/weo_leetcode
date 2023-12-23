import functools
import operator
from typing import List


class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        set_nums = set(nums)
        for i in range(32):
            if 1 << i not in set_nums:
                return 1 << i
        return -1


