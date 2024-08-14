from typing import List
from functools import cache


class Solution:
    def __init__(self) -> None:
        self.matrix = []

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row_cnt, col_cnt = len(matrix), len(matrix[0])
        @cache
        def max_seq(row_idx: int, col_idx: int) -> int:
            direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            ret = 1
            for d in direct:
                new_pos = [row_idx + d[0], col_idx + d[1]]
                if 0 <= new_pos[0] < row_cnt and 0 <= new_pos[1] < col_cnt:
                    if matrix[row_idx][col_idx] > matrix[new_pos[0]][new_pos[1]]:
                        ret = max(ret, max_seq(new_pos[0], new_pos[1]) + 1)
            return ret
        ans = 0
        for i in range(row_cnt):
            for j in range(col_cnt):
                ans = max(ans, max_seq(i, j))
        return ans


data = [[9,9,4],[6,6,8],[2,1,1]]
r = Solution().longestIncreasingPath(data)
print(r)

