from typing import List
import math


class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        ans = 0
        max_height = math.inf
        for height in maximumHeight:
            if min(height, max_height) <= 0:
                return -1
            ans += min(height, max_height)
            max_height = min(height, max_height) - 1
        return ans
