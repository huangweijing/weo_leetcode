from typing import List

class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        size = len(matrix)
        full_set = set[int]()
        for row_idx in range(size):
            if matrix[row_idx][col_idx] == 0:
                one_set1.add(row_idx)
            else:
                one_set2.add(row_idx)

        for col_idx in range(1, size):
            one_set1 = set[int]()
            one_set2 = set[int]()
            for row_idx in range(size):
                if matrix[row_idx][col_idx] == 0:
                    one_set1.add(row_idx)
                else:
                    one_set2.add(row_idx)
