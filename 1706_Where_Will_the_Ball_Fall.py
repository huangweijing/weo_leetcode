from typing import List

class Solution:
    def next_row(self, balls: list[set[int]], row: list[int]):
        new_balls = [set[int]() for _ in row]
        for i in range(len(row)):
            if (row[i] == -1 and i == 0) or (row[i] == 1 and i == len(row) - 1):
                continue
            if row[i] == 1 and row[i + 1] == 1:
                new_balls[i + 1] = new_balls[i + 1].union(balls[i])
            if row[i] == -1 and row[i - 1] == -1:
                new_balls[i - 1] = new_balls[i - 1].union(balls[i])
        return new_balls


    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        balls = [set[int]([i]) for i in range(n)]
        for row in grid:
            balls = self.next_row(balls, row)
        ans = [-1] * n
        for i, ball_set in enumerate(balls):
            for ball in ball_set:
                ans[ball] = i
        return ans

data = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
r = Solution().findBall(data)
print(r)


