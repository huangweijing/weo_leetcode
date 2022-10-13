from typing import List

class Solution:
    def __init__(self):
        self.cnt = 0
        self.grid = []
        self.space = 0

    def my_path(self, r: int, c: int, path_len: int, path: list[list[int]]):
        if self.grid[r][c] == 2:
            if self.space == path_len:
                # print(self.space, path_len, path)
                self.cnt += 1
            return
        # print(path)
        path.append([r, c])
        self.grid[r][c] = -2
        if r > 0 and self.grid[r - 1][c] in (0, 2):
            self.my_path(r - 1, c, path_len + 1, path)
        if r < len(self.grid) - 1 and self.grid[r + 1][c] in (0, 2):
            self.my_path(r + 1, c, path_len + 1, path)
        if c > 0 and self.grid[r][c - 1] in (0, 2):
            self.my_path(r, c - 1, path_len + 1, path)
        if c < len(self.grid[0]) - 1 and self.grid[r][c + 1] in (0, 2):
            self.my_path(r, c + 1, path_len + 1, path)
        self.grid[r][c] = 0
        path.pop()


    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.grid = grid
        r, c = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    r, c = i, j
                if grid[i][j] == 0:
                    self.space += 1
        # print(len(grid), len(grid[0]), self.space)
        path_len = 0
        if r > 0 and self.grid[r - 1][c] in (0, 2):
            self.my_path(r - 1, c, path_len, [])
        if r < len(grid) - 1 and self.grid[r + 1][c] in (0, 2):
            self.my_path(r + 1, c, path_len, [])
        if c > 0 and self.grid[r][c - 1] in (0, 2):
            self.my_path(r, c - 1, path_len, [])
        if c < len(grid[0]) - 1 and self.grid[r][c + 1] in (0, 2):
            self.my_path(r, c + 1, path_len, [])
        return self.cnt
#   0 1 2  3 4 5 6 7 8 9
#[[-1,0,1,-1]
#,[2, 0,0, 0]]
res = Solution().uniquePathsIII([[-1,0,1,-1],[2,0,0,0]])
print(res)
