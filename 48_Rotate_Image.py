from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        new_matrix :list[list[int]]() = [[0] * size for i in range(size)]

        for i in range(size):
            for j in range(size):
                new_matrix[j][size - 1 - i] = matrix[i][j]

        for i in range(size):
            for j in range(size):
                matrix[i][j] = new_matrix[i][j]

# sol = Solution()
# print(sol.rotate([
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3],
# ]))