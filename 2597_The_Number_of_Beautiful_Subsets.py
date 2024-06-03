from typing import List
from collections import Counter, defaultdict
import bisect


class Solution:
    def __init__(self):
        self.nums = []
        self.k = 0

    def my_sol(self, cur_sel: list[int], cur_idx: int) -> int:
        if cur_idx == len(self.nums):
            return 0
        ret = 0
        num = self.nums[cur_idx]
        idx = bisect.bisect_right(cur_sel, num - self.k) - 1
        if idx == -1 or idx == len(self.nums) or cur_sel[idx] != num - self.k:
            # print(idx, num)
            cur_sel.append(num)
            ret += self.my_sol(cur_sel, cur_idx + 1) + 1
            cur_sel.pop()
        ret += self.my_sol(cur_sel, cur_idx + 1)
        return ret

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        self.nums, self.k = nums, k
        return self.my_sol([], 0)


data = [
    [2,4,6,8,7,9,12,15,13]
    , 2
]
r = Solution().beautifulSubsets(* data)
print(r)
