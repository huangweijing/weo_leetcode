from functools import cache

class Solution:
    def __init__(self):
        self.nums = []

    @cache
    def max_money_robbed(self, k) -> int:
        if k == 0:
            return self.nums[0]
        if k == 1:
            return max(self.nums[0], self.nums[1])
        sol1 = self.max_money_robbed(k - 2) + self.nums[k]
        sol2 = self.max_money_robbed(k - 1)
        return max(sol1, sol2)

    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        for i in range(len(nums)):
            self.max_money_robbed(i)
        return self.max_money_robbed(len(nums) - 1)
