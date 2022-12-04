from typing import List
from collections import Counter
from functools import cache

class Solution:
    def __init__(self):
        self.s_cnt_arr = []

    @cache
    def my_find(self, length: int, m: int, n:int) -> int:
        # print(self.s_cnt_arr[: length], m, n)
        if m < 0 or n < 0:
            return -1
        if length == 0:
            return 0
        sub1 = self.my_find(length - 1, m, n)
        last_ele = self.s_cnt_arr[length - 1]
        sub2 = self.my_find(length - 1, m - last_ele["0"], n - last_ele["1"]) + 1
        return max(sub1, sub2)

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        for s in strs:
            self.s_cnt_arr.append(Counter(s))
        return self.my_find(len(strs), m, n)

data = [
    ["10", "0", "1"]
    , 1
    , 1
]
# data = [
#     ["10"]
#     , 1
#     , 1
# ]
r = Solution().findMaxForm(* data)
print(r)

