from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])

        transposed_matrix = [[0] * n for x in range(m)]
        for i in range(n):
            for j in range(m):
                # print(i, j)
                transposed_matrix[j][i] = matrix[i][j]

        return transposed_matrix

sol = Solution()
r = sol.transpose([[1,2,3],[4,5,6],[7,8,9]])
print(r)

# t = [[0] * 3 for i in range(4)]
# print(t)
# t[1][1] = 2
# print(t)