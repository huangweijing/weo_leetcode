from typing import List


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        n1_set, n2_set = set(nums1), set(nums2)
        # and_set = n1_set & n2_set
        or_set = n1_set | n2_set
        return min(min(len(n1_set), n >> 1) + min(len(n2_set), n >> 1), len(or_set))



