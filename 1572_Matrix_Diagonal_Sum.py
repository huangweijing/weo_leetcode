from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        side_len = len(mat)
        ans = 0
        for k in range(side_len):
            ans += mat[k][k] + mat[k][side_len - 1 - k]
        if side_len & 1 == 1:
            ans -= mat[side_len >> 1][side_len >> 1]
        return ans