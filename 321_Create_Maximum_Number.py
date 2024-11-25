from typing import List
from functools import cache


class Solution:
    def __init__(self) -> None:
        self.nums1 = []
        self.nums2 = []

    def my_sol(self, left1: int, left2: int, k: int) -> str:
        if k == 0:
            return ""
        if k == 1:
            return str(max(max(self.nums1[left1: ]), max(self.nums2[left2: ])))
        ret = ""
        if self.nums1[left1] > self.nums2[left2]:
            r1 = self.my_sol(left1 + 1, left2, k - 1)
            if r1 != "":
                ret = str(self.nums1[left1]) + r1
        else:
            r2 = self.my_sol(left1, left2 + 1, k - 1)
            if r2 != "":
                ret = str(self.nums1[left2]) + r2
        r3 = self.my_sol(left1, left2, k)
        if ret != "":
            if r3[0] >= ret[0]:
                ret = r3
        return ret

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        self.nums1, self.nums2 = nums1, nums2
        return self.my_sol(0, 0, k)


data = [
    [3,4,6,5]
    , [9,1,2,5,8,3]
    , 5
]
r = Solution().maxNumber(*data)
print(r)