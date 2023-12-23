from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_nums1, set_nums2 = set(nums1), set(nums2)
        ans = [0, 0]
        for num in nums1:
            if num in set_nums2:
                ans[0] += 1
        for num in nums2:
            if num in set_nums1:
                ans[1] += 1
        return ans

