from typing import List

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        paint_matrix = [[0] * (n + 1) for _ in range(n + 1)]
        ans = [[0] * n for _ in range(n)]
        for query in queries:
            row1, col1, row2, col2 = query[0], query[1], query[2], query[3]
            for i in range(row1, row2 + 1):
                paint_matrix[i][col1] += 1
                paint_matrix[i][col2 + 1] -= 1
        paint = 0
        # print(paint_matrix)
        for i in range(n):
            for j in range(n):
                paint += paint_matrix[i][j]
                ans[i][j] = paint
            paint += paint_matrix[i][n]
        return ans

data = [
    13
    , [[3,1,7,3],[7,5,7,8],[4,12,6,12],[2,8,6,11],[9,11,10,11],[9,3,11,11],[0,12,10,12],[10,5,11,12],[4,7,6,12],[0,2,9,6],[12,7,12,11],[2,7,3,8],[2,9,6,12],[10,7,10,12],[11,6,11,7],[3,2,12,9]]
]
r = Solution().rangeAddQueries(* data)
print(r)
