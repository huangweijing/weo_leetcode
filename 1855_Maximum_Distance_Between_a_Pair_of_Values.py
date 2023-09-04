from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        nums1, nums2 = nums1[::-1], nums2[::-1]
        # print(nums1)
        # print(nums2)
        p1, p2 = 0, 0
        ans = 0
        while p1 < len(nums1) and p2 < len(nums2):
            while p1 < len(nums1) and nums1[p1] <= nums2[p2]:
                # print(p1, p2)
                ans = max(ans, (len(nums2) - 1 - p2) - (len(nums1) - 1 - p1))
                # print(nums1[p1], nums2[p2])
                p1 += 1
            p2 += 1
            if (len(nums2) - 1 - p2) < (len(nums1) - 1 - p1):
                p1 += 1
        return ans

data = [
    [2]
    , [2, 2, 1]
]
r = Solution().maxDistance(* data)
print(r)