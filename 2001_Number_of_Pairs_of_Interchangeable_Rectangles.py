from typing import List
from collections import Counter


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio_dict = Counter()
        for rect in rectangles:
            ratio_dict[rect[0] / rect[1]] += 1
        return sum((cnt * (cnt - 1)) >> 1 for cnt in ratio_dict.values())

