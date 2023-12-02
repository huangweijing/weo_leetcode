from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # len_matrix = [[0] * len(matrix[0]) for _ in matrix]
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if col == 1:
                    if i > 0:
                        matrix[i][j] = matrix[i - 1][j] + 1
                    else:
                        matrix[i][j] = 1
                else:
                    matrix[i][j] = 0
        ans = 0
        for row in matrix:
            row.sort(reverse=True)
            for i, val in enumerate(row):
                ans = max(ans, val * (i + 1))
        return ans


data = [[0,0,1],[1,1,1],[1,0,1]]
r = Solution().largestSubmatrix(data)
print(r)



