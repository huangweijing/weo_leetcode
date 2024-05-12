from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_min, col_max = [], [0] * len(matrix[0])
        for i, row in enumerate(matrix):
            row_min.append(min(row))
            for j, val in enumerate(row):
                col_max[j] = max(col_max[j], val)
        ans = []
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if row_min[i] == val and col_max[j] == val:
                    ans.append(val)
        return ans

