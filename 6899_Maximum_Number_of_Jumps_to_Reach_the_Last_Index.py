from typing import List
from functools import cache

class Solution:
    def __init__(self):
        self.nums = []
        self.target = 0

    @cache
    def my_sol(self, idx: int) -> int:
        if idx == len(self.nums) - 1:
            return 0
        ans = -1
        for i in range(idx + 1, len(self.nums)):
            if abs(self.nums[idx] - self.nums[i]) <= self.target:
                sub_sol = self.my_sol(i)
                if sub_sol != -1:
                    ans = max(ans, sub_sol + 1)
        # print(idx, ans)
        return ans

    def maximumJumps(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        return self.my_sol(0)


data = [
    [1, 3, 6, 4, 1, 2]
    , 3
]
r = Solution().maximumJumps(* data)
print(r)

