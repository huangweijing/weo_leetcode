from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new_arr = list[int]()
        idx1, idx2 = 0, 0
        while idx1 < m or idx2 < n:
            if (not idx2 < n) or (idx1 < m and nums1[idx1] < nums2[idx2]):
                new_arr.append(nums1[idx1])
                idx1 += 1
            else:
                new_arr.append(nums2[idx2])
                idx2 += 1

        for i in range(len(new_arr)):
            nums1[i] = new_arr[i]

sol = Solution()
n1 = [1]
n2 = []
sol.merge(n1, len(n1) - len(n2), n2, len(n2))
print(n1)
