from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        max_row, max_col = m, n
        for op in ops:
            if op[0] < max_row:
                max_row = op[0]
            if op[1] < max_col:
                max_col = op[1]
        return max_row * max_col