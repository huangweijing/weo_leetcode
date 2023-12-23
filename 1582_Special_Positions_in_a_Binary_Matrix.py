from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_sum, col_sum = [], []
        for row in mat:
            row_sum.append(sum(row))
        for i in range(len(mat[0])):
            col = 0
            for j in range(len(mat)):
                col += mat[j][i]
            col_sum.append(col)
        ans = 0
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if val == row_sum[i] == col_sum[j] == 1:
                    ans += 1
        return ans

