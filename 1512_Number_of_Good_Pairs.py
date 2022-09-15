from typing import List
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_cnt = Counter(nums)
        return sum([int(val * (val - 1) / 2) for key, val in num_cnt.items() if val > 1])