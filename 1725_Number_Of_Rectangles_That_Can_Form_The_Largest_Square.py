from typing import List
from collections import Counter



class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        cnt = Counter()
        max_len = 0
        for rect in rectangles:
            sqr_side = min(rect)
            max_len = max(max_len, sqr_side)
            cnt[sqr_side] += 1
        return cnt[max_len]

