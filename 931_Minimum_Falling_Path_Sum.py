from typing import List
import math
from functools import cache

class Solution:
    def __init__(self):
        self.dp = []
        self.matrix = []
        self.n = 0

    @cache
    def get_min(self, row: int, col: int):
        if row == 0:
            return self.matrix[row][col]
        ans = self.matrix[row][col] + self.get_min(row - 1, col)
        if col - 1 >= 0:
            ans = min(self.matrix[row][col] + self.get_min(row - 1, col - 1), ans)
        if col + 1 < self.n:
            ans = min(self.matrix[row][col] + self.get_min(row - 1, col + 1), ans)
        return ans

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        self.n = len(matrix)
        self.matrix = matrix
        self.dp = [[math.inf] * self.n for _ in range(self.n)]
        ans = math.inf
        for i in range(self.n):
            ans = min(self.get_min(self.n - 1, i), ans)
        return ans

data = [[2,1,3],[6,5,4],[7,8,9]]
r = Solution().minFallingPathSum(data)
print(r)
