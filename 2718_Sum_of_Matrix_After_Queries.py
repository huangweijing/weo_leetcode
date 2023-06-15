from typing import List


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row_idx_set = set[int]()
        col_idx_set = set[int]()
        ans = 0
        while len(queries) > 0:
            query = queries.pop()
            query_type, idx, val = query[0], query[1], query[2]
            if query_type == 0:
                if idx in row_idx_set:
                    continue
                else:
                    row_idx_set.add(idx)
                    ans += (n - len(col_idx_set)) * val
            elif query_type == 1:
                if idx in col_idx_set:
                    continue
                else:
                    col_idx_set.add(idx)
                    ans += (n - len(row_idx_set)) * val
        return ans