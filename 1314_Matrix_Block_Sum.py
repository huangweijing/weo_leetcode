from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        sum_from_left_top = [[0] * n for _ in range(m)]
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            sum_from_left = 0
            for j in range(n):
                sum_from_left += mat[i][j]
                if i > 0:
                    sum_from_left_top[i][j] = sum_from_left + sum_from_left_top[i - 1][j]
                else:
                    sum_from_left_top[i][j] = sum_from_left
        # print(sum_from_left_top)
        for i in range(m):
            for j in range(n):
                top, bottom, left, right = i - k - 1, i + k, j - k - 1, j + k
                bottom = m - 1 if bottom >= m else bottom
                right = n - 1 if right >= n else right

                left_top_block, left_block, right_block = 0, 0, 0
                if left >= 0 and top >= 0:
                    left_top_block = sum_from_left_top[top][left]
                if left >= 0:
                    left_block = sum_from_left_top[bottom][left]
                if top >= 0:
                    right_block = sum_from_left_top[top][right]
                bottom_right_block = sum_from_left_top[bottom][right]

                ans[i][j] = bottom_right_block - left_block - right_block + left_top_block
                # print(f"i={i}, j={j}, lt={left_top_block}, l={left_block}, r={right_block}, br={bottom_right_block}")
        return ans

data = [
    [[67, 64, 78], [99, 98, 38], [82, 46, 46], [6, 52, 55], [55, 99, 45]]
    ,3
]
r = Solution().matrixBlockSum(* data)
print(r)
