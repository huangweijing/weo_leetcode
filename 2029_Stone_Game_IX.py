from typing import List
from collections import Counter


class Solution:
    def my_sol(self, c0: int, c1: int, c2: int) -> bool:
        pass

    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = Counter()
        for stone in stones:
            cnt[stone % 3] += 1
        