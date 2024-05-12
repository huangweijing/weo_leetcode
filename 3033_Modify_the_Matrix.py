from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        col_max = []
        for i in range(len(matrix[0])):
            col_max.append(max(row[i] for row in matrix))
        for i in range(len(matrix[0])):
            for row in matrix:
                if row[i] == -1:
                    row[i] = col_max[i]
        return matrix
