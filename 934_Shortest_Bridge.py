from typing import List


class Solution:
    def __init__(self):
        self.n = 0
        self.grid = [[0]]
        self.color_set = dict[int, set[int]]()
        self.color_set[2] = set[int]()
        self.color_set[3] = set[int]()
        self.end = False

    def dfs(self, start: list[int], grid: list[list[int]], color: int):
        n = self.n
        row, col = start[0], start[1]
        grid[row][col] = color
        self.color_set[color].add(row * n + col)
        if col + 1 < n and grid[row][col + 1] == 1:
            self.dfs([row, col + 1], grid, color)
        if col > 0 and grid[row][col - 1] == 1:
            self.dfs([row, col - 1], grid, color)
        if row > 0 and grid[row - 1][col] == 1:
            self.dfs([row - 1, col], grid, color)
        if row + 1 < n and grid[row + 1][col] == 1:
            self.dfs([row + 1, col], grid, color)

    def bfs(self, start: list[int], grid: list[list[int]], color: int) -> set[int]:
        n = self.n
        row, col = start[0], start[1]
        filled = set[int]()
        if col + 1 < n and grid[row][col + 1] != color:
            if grid[row][col + 1] != 0:
                self.end = True
                return filled
            grid[row][col + 1] = color
            filled.add(row * n + col + 1)
        if col > 0 and grid[row][col - 1] != color:
            if grid[row][col - 1] != 0:
                self.end = True
                return filled
            grid[row][col - 1] = color
            filled.add(row * n + col - 1)
        if row > 0 and grid[row - 1][col] != color:
            if grid[row - 1][col] != 0:
                self.end = True
                return filled
            grid[row - 1][col] = color
            filled.add((row - 1)* n + col)
        if row + 1 < n and grid[row + 1][col] != color:
            if grid[row + 1][col] != 0:
                self.end = True
                return filled
            grid[row + 1][col] = color
            filled.add((row + 1)* n + col)
        return filled

    def shortestBridge(self, grid: List[List[int]]) -> int:
        self.grid = grid
        n = len(grid)
        self.n = n
        color = 2
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    self.dfs([row, col], grid, color)
                    color += 1
        filled_set = self.color_set[2]
        # print(grid)
        ans = 0
        while len(filled_set) > 0:
            new_filled_set = set[int]()
            while len(filled_set) > 0:
                pos = filled_set.pop()
                row, col = pos // n, pos % n
                new_set = self.bfs([row, col], grid, grid[row][col])
                # print(row, col, filled_set, grid)
                if self.end:
                    return ans
                new_filled_set = new_filled_set.union(new_set)
            filled_set = new_filled_set
            ans += 1
        return ans

data = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
r = Solution().shortestBridge(data)
print(r)



