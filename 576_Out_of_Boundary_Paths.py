from functools import cache

class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.dp = []
        self.start_row = 0
        self.start_col = 0

    def init_grid(self):
        grid = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            grid[i][0] += 1
            grid[i][self.n - 1] += 1
        for i in range(self.n):
            grid[0][i] += 1
            grid[self.m - 1][i] += 1
        return grid

    def next_grid(self, grid: list[list[int]], new_grid: list[list[int]]):
        for i in range(self.m):
            for j in range(self.n):
                new_grid[i][j] = 0
                if j + 1 < self.n:
                    new_grid[i][j] += grid[i][j + 1]
                if j - 1 >= 0:
                    new_grid[i][j] += grid[i][j - 1]
                if i + 1 < self.m:
                    new_grid[i][j] += grid[i + 1][j]
                if i - 1 >= 0:
                    new_grid[i][j] += grid[i - 1][j]

    def copy_grid(self, from_grid: list[list[int]], to_grid: list[list[int]]):
        for i, row in enumerate(from_grid):
            to_grid[i] = row.copy()

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0:
            return 0
        self.m, self.n, self.start_row, self.start_col = m, n, startRow, startColumn
        self.dp = [[[0] * n for _ in range(m)] for _ in range(2)]
        self.dp[0] = self.init_grid()
        print(self.dp[0])
        ans = self.dp[0][startRow][startColumn]
        for i in range(1, maxMove):
            self.next_grid(self.dp[0], self.dp[1])
            self.copy_grid(self.dp[1], self.dp[0])
            ans += self.dp[0][startRow][startColumn]
        print(self.dp)
        return ans % (10 ** 9 + 7)

data = [3
, 8
, 0
, 2
, 0]
r = Solution().findPaths(* data)
print(r)
