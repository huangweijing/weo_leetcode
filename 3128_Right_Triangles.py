from collections import Counter
from typing import List

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        row_cross_cnt = Counter()
        col_cross_cnt = Counter()
        cross_point_arr = []
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    cross_point_arr.append([i, j])
                    row_cross_cnt[i] += 1
                    col_cross_cnt[j] += 1
        ans = 0
        for p in cross_point_arr:
            ans += (row_cross_cnt[p[0]] - 1) * (col_cross_cnt[p[1]] - 1)
        return ans
