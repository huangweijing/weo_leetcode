from typing import List
from functools import cache


class Solution:
    def __init__(self) -> None:
        self.nums = []

    @cache
    def my_sol(self, left: int, right: int, score: int) -> int:
        sol1, sol2, sol3 = 0, 0, 0
        if 0 <= left < right < len(self.nums):
            # if self.nums[left] + self.nums[right] == score:
            #     sol1 = self.my_sol(left + 1, right - 1, score) + 1
            
            if self.nums[left] + self.nums[left + 1] == score:
                sol2 = self.my_sol(left + 2, right, score) + 1

            # if self.nums[right] + self.nums[right - 1] == score:
            #     sol3 = self.my_sol(left, right - 2, score) + 1
        # print(f"left={left}, right={right}, self.nums[left: right + 1]={self.nums[left: right + 1]}, max(sol1, sol2, sol3)={max(sol1, sol2, sol3)}, score={score}")
        # return max(sol1, sol2, sol3)
        return sol2

    def maxOperations(self, nums: List[int]) -> int:
        self.nums = nums
        # sol1 = self.my_sol(1, len(nums) - 2, nums[0] + nums[-1]) + 1
        sol2 = self.my_sol(2, len(nums) - 1, nums[0] + nums[1]) + 1
        # sol3 = self.my_sol(0, len(nums) - 3, nums[-1] + nums[-2]) + 1
        # return max(sol1, sol2, sol3)
        return sol2

        