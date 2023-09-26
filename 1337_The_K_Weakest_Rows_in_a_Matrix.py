from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_info_arr = []
        for i, row in enumerate(mat):
            row_info_arr.append([sum(row), i])
        row_info_arr.sort()
        return [x[1] for x in row_info_arr[: k]]
