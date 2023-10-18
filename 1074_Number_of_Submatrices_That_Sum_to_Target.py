from typing import List
from collections import Counter


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        prefix_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        row_prefix_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i, row in enumerate(matrix):
            prefix_sum = 0
            for j, val in enumerate(row):
                prefix_sum += val
                prefix_matrix[i][j] = prefix_sum
                row_prefix_matrix[i][j] = row_prefix_matrix[i - 1][j] + prefix_sum

        # print(row_prefix_matrix)
        # print(prefix_matrix)
        ans = 0
        for j in range(len(matrix[0])):
            for k in range(j + 1, len(matrix[0])):
                prefix_dict = Counter()
                prefix_dict[0] = 1
                for i, row in enumerate(row_prefix_matrix):
                    diff = row_prefix_matrix[i][k] - row_prefix_matrix[i][j]
                    ans += prefix_dict[diff - target]
                    prefix_dict[diff] += 1
        for k in range(len(matrix[0])):
            prefix_dict = Counter()
            prefix_dict[0] = 1
            for i, row in enumerate(row_prefix_matrix):
                diff = row_prefix_matrix[i][k]
                ans += prefix_dict[diff - target]
                prefix_dict[diff] += 1

        return ans


data = [
    [
        [1, 1, 1]
        , [1, 1, 1]
        , [1, 1, 1]
    ], 1
]
r = Solution().numSubmatrixSumTarget(*data)
print(r)

