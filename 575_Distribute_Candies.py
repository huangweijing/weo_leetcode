from typing import List
from collections import Counter

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        type_cnt = Counter(candyType)
        result = 0
        suspended = 0
        remained = 0
        for key, val in type_cnt.items():
            if val > 1:
                result += 1
                remained += val - 2
            else:
                suspended += 1
        if remained >= suspended:
            return result + suspended
        else:
            return result + remained + (suspended - remained >> 1)
