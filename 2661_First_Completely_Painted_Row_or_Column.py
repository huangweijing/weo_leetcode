from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_size, col_size = [0] * m, [0] * n
        row_map, col_map = dict[int, int](), dict[int, int]()
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                row_map[val] = i
                col_map[val] = j
        for i, val in enumerate(arr):
            row_idx = row_map[val]
            col_idx = col_map[val]
            row_size[row_idx] += 1
            col_size[col_idx] += 1
            if row_size[row_idx] == n or\
                    col_size[col_idx] == m:
                return i
        return 0

data = [
    [1,4,5,2,6,3]
    , [[4,3,5],[1,2,6]]
]
r = Solution().firstCompleteIndex(* data)
print(r)

