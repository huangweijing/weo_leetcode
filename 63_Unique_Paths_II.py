from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        matrix = [[0] * n for i in range(m)]
        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    continue
                cnt = 0
                if row == col == 0:
                    cnt = 1
                if row - 1 >= 0:
                    cnt += matrix[row - 1][col]
                if col - 1 >= 0:
                    cnt += matrix[row][col - 1]
                matrix[row][col] = cnt
        return matrix[m - 1][n - 1]


sol = Solution()
r = sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
print(r)
