from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for i, row in enumerate(matrix):
            if len(set(row)) != len(matrix):
                return False
        for i in range(len(matrix)):
            if len(set([matrix[j][i] for j in range(len(matrix))])) != len(matrix):
                return False
        return True

