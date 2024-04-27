from typing import List
from collections import deque


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds = deque()
        for num in arr:
            if num & 1 == 0:
                odds.clear()
                continue
            odds.append(num)
            if len(odds) == 3:
                return True
        return False


