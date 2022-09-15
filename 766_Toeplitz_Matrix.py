from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for col in range(m):
            diag_set = set[int]()
            for i in range(n):
                cell_row, cell_col = i, col + i
                if 0 <= cell_row < n and 0 <= cell_col < m:
                    diag_set.add(matrix[cell_row][cell_col])
            if len(diag_set) != 1:
                return False

        for row in range(1, n):
            diag_set = set[int]()
            for i in range(m):
                cell_row, cell_col = row + i, i
                if 0 <= cell_row < n and 0 <= cell_col < m:
                    diag_set.add(matrix[cell_row][cell_col])
            if len(diag_set) != 1:
                return False
        return True




