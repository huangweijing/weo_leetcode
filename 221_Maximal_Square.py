from functools import cache
from typing import List

class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.matrix = list[list[int]]()

    @cache
    def max_square(self, i: int, j: int) -> int:
        if self.matrix[i][j] == "0":
            return 0
        if i > 0 and j > 0:
            square_size = self.max_square(i - 1, j - 1)
            # print(square_size)
            if square_size == 0:
                return 1
            else:
                side_size1 = 0
                for idx in range(i, i - square_size - 1, -1):
                    # print(f"self.matrix[idx][j]={self.matrix[idx][j]}")
                    if self.matrix[idx][j] == "1":
                        side_size1 += 1
                    else:
                        break
                side_size2 = 0
                for idx in range(j, j - square_size - 1, -1):
                    # print(f"self.matrix[idx][j]={self.matrix[i][idx]}")
                    if self.matrix[i][idx] == "1":
                        side_size2 += 1
                    else:
                        break
                return min(side_size1, side_size2)
        else:
            return 1

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrix = matrix
        max_size = 0
        for i in range(self.m):
            for j in range(self.n):
                size = self.max_square(i, j)
                if size > max_size:
                    max_size = size
        return max_size ** 2

data_matrix = [["0","0","0","1"],["1","1","1","1"],["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]
sol = Solution()
r = sol.maximalSquare(data_matrix)
print()
print(sol.max_square(4, 3))
print(r)