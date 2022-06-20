class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0] * n for i in range(m)]
        for row in range(m):
            for col in range(n):
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
r = sol.uniquePaths(3, 7)
print(r)


