from typing import List
from functools import cache
import bisect

class Solution:
    def __init__(self):
        self.nums = []
        self.num_dict = dict[int, list[int]]()

    @cache
    def my_sol(self, n):
        if n == 0:
            return 1
        ans = self.my_sol(n - 1)
        for i in range(n):
            step = self.nums[n] - self.nums[i]
            ans = max(ans, self.my_sol_step(i, step) + 1)
        return ans

    @cache
    def my_sol_step(self, n: int, step: int):
        seq_len = 1
        val = self.nums[n] - step
        if val in self.num_dict:
            num_list = self.num_dict[val]
            for i in reversed(num_list):
                if i < n:
                    return self.my_sol_step(i, step) + 1
        return seq_len


    def longestArithSeqLength(self, nums: List[int]) -> int:
        self.nums = nums
        for i, num in enumerate(self.nums):
            if num not in self.num_dict:
                self.num_dict[num] = list[int]()
            self.num_dict[num].append(i)
        return self.my_sol(len(nums) - 1)


sol = Solution()
r = sol.longestArithSeqLength([3,6,9,12])
# r = sol.my_sol_step(3, 3)
print(r)