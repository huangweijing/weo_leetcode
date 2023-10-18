from functools import cache
import math


class Solution:
    def __init__(self):
        self.diff_arr = []
        self.x = 1

    @cache
    def my_sol(self, idx: int) -> int:
        if idx >= len(self.diff_arr):
            return math.inf
        if len(self.diff_arr) - 1 == idx:
            return self.x / 2
        if len(self.diff_arr) - 1 - idx == 1:
            return min(self.diff_arr[idx + 1] - self.diff_arr[idx]
                       , self.x)
        # print(idx)
        s1 = self.diff_arr[idx + 1] - self.diff_arr[idx] + self.my_sol(idx + 2)
        s2 = self.x / 2 + self.my_sol(idx + 1)
        return min(s1, s2)

    def minOperations(self, s1: str, s2: str, x: int) -> int:
        diff_arr = []
        for idx in range(len(s1)):
            if s1[idx] != s2[idx]:
                diff_arr.append(idx)
        if len(diff_arr) & 1 == 1:
            return -1
        if len(diff_arr) == 0:
            return 0
        # print(diff_arr)
        self.diff_arr = diff_arr
        self.x = x
        return int(self.my_sol(0))


data = [
    "00010"
    , "00010"
    , 2
]
r = Solution().minOperations(*data)
print(r)