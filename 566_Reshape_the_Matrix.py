from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        result = []
        new_row = []
        for row in mat:
            for cell in row:
                new_row.append(cell)
                if len(new_row) % c == 0:
                    result.append(new_row)
                    new_row = []
        return result

