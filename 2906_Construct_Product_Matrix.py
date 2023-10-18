import math
from typing import List
from collections import Counter, deque


class Solution:
    MOD = 12345
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        row_product = []
        row_product_prefix_matrix = []
        row_product_postfix_matrix = []
        for i, row in enumerate(grid):
            row_product_prefix = []
            row_product_postfix = deque()
            prefix_product = 1
            for j, val in enumerate(row):
                row_product_prefix.append(prefix_product)
                prefix_product = val * prefix_product % Solution.MOD
            postfix_product = 1
            for j, val in enumerate(reversed(row)):
                row_product_postfix.appendleft(postfix_product)
                postfix_product = val * postfix_product % Solution.MOD
            row_product.append(postfix_product)
            row_product_prefix_matrix.append(row_product_prefix)
            row_product_postfix_matrix.append(row_product_postfix)

        row_prefix = 1
        matrix_product_prefix = []
        matrix_product_postfix = deque()
        for i, row in enumerate(row_product):
            matrix_product_prefix.append(row_prefix)
            row_prefix *= row
        row_postfix = 1
        for i, row in enumerate(reversed(row_product)):
            matrix_product_postfix.appendleft(row_postfix)
            row_postfix *= row

        ans = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i, row in enumerate(ans):
            # print(row)
            for j in range(len(row)):
                row[j] = matrix_product_prefix[i] * matrix_product_postfix[i] % Solution.MOD
                row[j] = row[j] * row_product_prefix_matrix[i][j] % Solution.MOD
                row[j] = row[j] * row_product_postfix_matrix[i][j] % Solution.MOD
        return ans



data = [
[[1,2],[3,4]]
]
r = Solution().constructProductMatrix(*data)
print(r)
# print(1000000 % 12345)

