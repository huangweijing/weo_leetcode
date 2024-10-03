from typing import List
from functools import cache


class Solution:
    def __init__(self) -> None:
        self.arr = []
        self.d = -1

    @cache
    def max_cnt(self, idx: int) -> int:
        ret = 1
        for i in range(1, self.d + 1):
            if 0 <= idx + i < len(self.arr):
                if self.arr[idx] <= self.arr[idx + i]:
                    break
                ret = max(ret, self.max_cnt(idx + i) + 1)
        for i in range(1, self.d + 1):
            if 0 <= idx - i < len(self.arr):
                if self.arr[idx] <= self.arr[idx - i]:
                    break
                ret = max(ret, self.max_cnt(idx - i) + 1)
        return ret

    def maxJumps(self, arr: List[int], d: int) -> int:
        self.arr, self.d = arr, d
        ans = 0
        for i in range(len(arr)):
            ans = max(ans, self.max_cnt(i))
            # print(i, arr[i], self.max_cnt(i))
        return ans


data = [
    [6,4,14,6,8,13,9,7,10,6,12]
    , 2
    # [3, 3, 3]
    # , 1
]
r = Solution().maxJumps(* data)
print(r)