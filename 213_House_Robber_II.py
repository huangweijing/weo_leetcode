from functools import cache

class Solution:
    def __init__(self):
        self.nums = []

    @cache
    def max_money_robbed(self, k: int, robbed_h1: bool) -> int:
        if k < 0:
            return 0
        if k == 0 and robbed_h1:
            return self.nums[0]
        if k == 0 and not robbed_h1:
            return 0
        if k == 1:
            return max(self.nums[k], self.max_money_robbed(0, robbed_h1))
        sol1 = self.max_money_robbed(k - 2, robbed_h1) + self.nums[k]
        sol2 = self.max_money_robbed(k - 1, robbed_h1)
        return max(sol1, sol2)

    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        for i in range(len(nums)):
            self.max_money_robbed(i, True)
            self.max_money_robbed(i, False)

        r1 = self.max_money_robbed(len(nums) - 1, False)
        r2 = self.max_money_robbed(len(nums) - 2, True)
        r3 = self.max_money_robbed(len(nums) - 2, False)
        return max(r1, r2, r3, nums[0])
