from typing import List
from collections import deque
from functools import cache

class Solution:
    def __init__(self):
        self.nums = []

    @cache
    def highest_scores(self, left: int, right: int) -> (int, int):
        if left == right:
            return self.nums[left], 0
        opp_score1, score1 = self.highest_scores(left + 1, right)
        opp_score2, score2 = self.highest_scores(left, right - 1)
        diff1 = score1 + self.nums[left] - opp_score1
        diff2 = score2 + self.nums[right] - opp_score2
        if diff1 > diff2:
            return score1 + self.nums[left], opp_score1
        else:
            return score2 + self.nums[right], opp_score2

    def PredictTheWinner(self, nums: List[int]) -> bool:
        self.nums = nums
        score, opp_score = self.highest_scores(0, len(nums) - 1)
        return score >= opp_score

data = [1,5,233,7]
r = Solution().PredictTheWinner(data)
print(r)

