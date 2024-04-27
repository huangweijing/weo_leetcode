from typing import List


class Solution:
    def __init__(self):
        self.n = 0

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        self.n = len(mat)
        for i in range(4):
            is_okay = True
            for row_idx in range(len(mat)):
                for col_idx in range(len(mat[row_idx])):
                    new_row, new_col = self.rotate(row_idx, col_idx, i)
                    if mat[row_idx][col_idx] != target[new_row][new_col]:
                        is_okay = False
                        break
                if not is_okay:
                    break
            if is_okay:
                return True
        return False

    def rotate(self, x: int, y: int, cnt: int) -> (int, int):
        if cnt == 0:
            return x, y
        else:
            return self.rotate(y, self.n - 1 - x, cnt - 1)

