from typing import List

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        union_set = set(nums1) & set(nums2)
        if len(union_set) > 0:
            return min(union_set)
        dig1, dig2 = min(nums1), min(nums2)
        return min(dig1 * 10 + dig2, dig2 * 10 + dig1)
