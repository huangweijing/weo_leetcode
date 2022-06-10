from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        result :list[int] = []
        direction = 0
        row: int = 0
        col: int = 0
        min_row, max_row, min_col, max_col = 0, m - 1, 0, n - 1
        # print(min_row, max_row, min_col, max_col)
        for i in range(m * n):
            # print(row, col, matrix[row][col], direction)
            result.append(matrix[row][col])
            if direction == 0:
                if col == max_col:
                    direction = 1
                    min_row += 1
                    row += 1
                else:
                    col += 1
            elif direction == 1:
                if row == max_row:
                    direction = 2
                    max_col -= 1
                    col -= 1
                else:
                    row += 1
            elif direction == 2:
                if col == min_col:
                    direction = 3
                    max_row -= 1
                    row -= 1
                else:
                    col -= 1
            elif direction == 3:
                if row == min_row:
                    direction = 0
                    min_col += 1
                    col += 1
                else:
                    row -= 1
        return result

sol = Solution()
r = sol.spiralOrder([
    [1, 2, 3, 4, 5]
    , [6, 7, 8, 9, 10]
    , [11, 12, 13, 14, 15]
    , [16, 17, 18, 19, 20]
    , [21, 22, 23, 24, 25]
])
print(r)