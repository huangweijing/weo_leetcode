from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_set, nums2_set = set(nums1), set(nums2)
        common_set = nums1_set.intersection(nums2_set)
        if len(common_set) == 0:
            return -1
        return min(common_set)