from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row_cnt, col_cnt = len(mat), len(mat[0])
        row_idx, col_idx = 0, 0
        ans = []
        dir_row, dir_col = -1, 1
        for _ in range(row_cnt * col_cnt):
            print(mat[row_idx][col_idx])
            ans.append(mat[row_idx][col_idx])
            if row_idx == 0 and col_idx < col_cnt - 1 and [dir_row, dir_col] == [-1, 1]:
                row_idx, col_idx = 0, col_idx + 1
                dir_row, dir_col = 1, -1
            elif col_idx == col_cnt - 1 and [dir_row, dir_col] == [-1, 1]:
                row_idx, col_idx = row_idx + 1, col_cnt - 1
                dir_row, dir_col = 1, -1
            elif row_idx == row_cnt - 1 and [dir_row, dir_col] == [1, -1]:
                row_idx, col_idx = row_cnt - 1, col_idx + 1
                dir_row, dir_col = [-1, 1]
            elif col_idx == 0 and [dir_row, dir_col] == [1, -1]:
                # print("lalala")
                row_idx, col_idx = row_idx + 1, 0
                dir_row, dir_col = [-1, 1]
            else:
                row_idx += dir_row
                col_idx += dir_col
            # print("new idx=", row_idx, col_idx)
        return ans
    

data = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
r = Solution().findDiagonalOrder(data)
print(r)
            