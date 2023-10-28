from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        prefix_xor_sum = [[0] * n for _ in range(m)]
        val_matrix = [[0] * n for _ in range(m)]
        val_list = []
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if j == 0:
                    prefix_xor_sum[i][j] = val
                else:
                    prefix_xor_sum[i][j] = prefix_xor_sum[i][j - 1] ^ val
                if i == 0:
                    val_matrix[i][j] = prefix_xor_sum[i][j]
                else:
                    val_matrix[i][j] = prefix_xor_sum[i][j] ^ val_matrix[i - 1][j]
                val_list.append(val_matrix[i][j])
        val_list.sort(reverse=True)

        return val_list[k - 1]
