from typing import List
from collections import defaultdict

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        row_mine = defaultdict(lambda: list[int]())
        col_mine = defaultdict(lambda: list[int]())
        left, right, up, down = dict[tuple[int, int], int](), \
            dict[tuple[int, int], int](), \
            dict[tuple[int, int], int](), \
            dict[tuple[int, int], int]()
        for mine in mines:
            row_mine[mine[0]].append(mine[1])
            col_mine[mine[1]].append(mine[0])
        for row in row_mine.keys():
            row.sort()
            for i, col_idx in enumerate(row):
                if i > 0 and row[i - 1] + 1 == col_idx:
                    left[(i, col_idx)] = left[(i, row[i - 1])] + 1
                else:
                    left[(i, col_idx)] = 1
            for j, col_idx in enumerate(reversed(row)):
                i = len(row) - 1 - j
                if i < len(row) - 1 and row[i + 1] - 1 == col_idx:
                    right[(i, col_idx)] = left[(i, row[i + 1])] + 1
                else:
                    right[(i, col_idx)] = 1

        for col in col_mine.values():
            col.sort()
            for i, row_idx in enumerate(col):
                if i > 0 and col[i - 1] + 1 == row_idx:
                    up[(row_idx, i)] = up[(col[i - 1], i)] + 1
                else:
                    up[(row_idx, i)] = 1
            for j, row_idx in enumerate(reversed(col)):
                i = len(col) - 1 - j
                if i < len(col) - 1 and col[i + 1] - 1 == row_idx:
                    down[(row_idx, i)] = down[(col[i - 1], i)] + 1
                else:
                    down[(row_idx, i)] = 1
        
        ans = 0
        for item in down:
            ans = max(ans, min(up[item], down[item], left[item], right[item]))
        return ans


data = [
    5
    , [[4,2]]
]
r = Solution().orderOfLargestPlusSign(*data)
print(r)