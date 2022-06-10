from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for i in range(n)]
        m = len(matrix)
        n = len(matrix[0])
        direction = 0
        row: int = 0
        col: int = 0
        min_row, max_row, min_col, max_col = 0, m - 1, 0, n - 1
        # print(min_row, max_row, min_col, max_col)
        for i in range(m * n):
            # print(row, col, matrix[row][col], direction)
            # result.append(matrix[row][col])
            matrix[row][col] = i + 1
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
        return matrix

sol = Solution()
r = sol.generateMatrix(5)
print(r)