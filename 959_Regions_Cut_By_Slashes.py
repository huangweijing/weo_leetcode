from typing import List
from collections import deque

class Solution:
    def __init__(self):
        self.color_grid = []
        self.grid = []
        self.n = 0
        self.ans = set()

    def paint(self, row: int, col: int, direction: int, color: int):
        ch = self.grid[row][col]
        if ch == " ":
            if self.color_grid[row][col] != [0, 0]:
                return
            self.ans.add(color)
            self.color_grid[row][col] = [color, color]
            if row > 0:
                self.paint(row - 1, col, 1, color)
            if row < self.n - 1:
                self.paint(row + 1, col, 0, color)
            if col > 0:
                self.paint(row, col - 1, 3, color)
            if col < self.n - 1:
                self.paint(row, col + 1, 2, color)
        elif ch == "/":
            if direction in (0, 2):
                if self.color_grid[row][col][0] != 0:
                    return
                self.ans.add(color)
                self.color_grid[row][col][0] = color
                if row > 0:
                    self.paint(row - 1, col, 1, color)
                if col > 0:
                    self.paint(row, col - 1, 3, color)
            else:
                if self.color_grid[row][col][1] != 0:
                    return
                self.ans.add(color)
                self.color_grid[row][col][1] = color
                if row < self.n - 1:
                    self.paint(row + 1, col, 0, color)
                if col < self.n - 1:
                    self.paint(row, col + 1, 2, color)
        elif ch == "\\":
            if direction in (0, 3):
                if self.color_grid[row][col][1] != 0:
                    return
                self.ans.add(color)
                self.color_grid[row][col][1] = color
                if row > 0:
                    self.paint(row - 1, col, 1, color)
                if col < self.n - 1:
                    self.paint(row, col + 1, 2, color)
            else:
                if self.color_grid[row][col][0] != 0:
                    return
                self.ans.add(color)
                self.color_grid[row][col][0] = color
                if col > 0:
                    self.paint(row, col - 1, 3, color)
                if row < self.n - 1:
                    self.paint(row + 1, col, 0, color)

    def regionsBySlashes(self, grid: List[str]) -> int:
        self.n = len(grid)
        self.grid = grid
        self.color_grid = [[[0, 0] for _ in range(self.n)] for _ in range(self.n)]

        color_cnt = 0
        color = 1
        for row in range(self.n):
            for col in range(self.n):

                self.paint(row, col, 0, color)
                color += 1
                new_color_cnt = len(self.ans)
                if color_cnt != new_color_cnt:
                    print(self.color_grid)
                    color_cnt = new_color_cnt

                self.paint(row, col, 1, color)
                new_color_cnt = len(self.ans)
                if color_cnt != new_color_cnt:
                    color_cnt = new_color_cnt
                    print(self.color_grid)
                color += 1
        print(self.color_grid)
        # print(self.ans)
        return len(self.ans)

data = ["\\/\\ ", " //\\", " //\\", "\\\\\\/"]
r = Solution().regionsBySlashes(data)
print(r)
