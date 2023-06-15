from typing import List
import bisect


class Solution:

    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for row in grid:
            for cell in row:
                if cell < 0:
                    ans += 1
        return ans