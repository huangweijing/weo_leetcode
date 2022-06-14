from typing import List

class Solution:
    def __init__(self):
        self.triangle: list[list[int]] = None
        self.solution = [[None] * 200 for i in range(200)]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.triangle = triangle
        return self.calc_min_path(0, 0)

    def calc_min_path(self, row_idx: int, col_idx) -> int:
        if self.solution[row_idx][col_idx] is not None:
            return self.solution[row_idx][col_idx]
        if row_idx == len(self.triangle) - 1:
            return self.triangle[row_idx][col_idx]
        min_path1 = self.calc_min_path(row_idx + 1, col_idx)
        min_path2 = self.calc_min_path(row_idx + 1, col_idx + 1)
        min_path = min_path1 if min_path1 < min_path2 else min_path2
        min_path += self.triangle[row_idx][col_idx]
        self.solution[row_idx][col_idx] = min_path
        return min_path

sol = Solution()
r = sol.minimumTotal([[-10]])
print(r)