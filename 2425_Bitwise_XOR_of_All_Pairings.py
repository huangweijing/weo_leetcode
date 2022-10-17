import operator
from typing import List
from functools import reduce

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        len_nums1, len_nums2 = len(nums1), len(nums2)
        nums = []
        if len_nums1 & 1 == 1:
            nums.extend(nums2)
        if len_nums2 & 1 == 1:
            nums.extend(nums1)
        if len(nums) == 0:
            return 0
        return reduce(operator.xor, nums)
