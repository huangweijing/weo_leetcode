from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        zero_col_list = set[int]()
        zero_row_list = set[int]()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_row_list.add(i)
                    zero_col_list.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zero_row_list or j in zero_col_list:
                    matrix[i][j] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
Solution().setZeroes(matrix)
print(matrix)