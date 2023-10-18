import math
from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        min_r, max_r, min_c, max_c = rStart, rStart, cStart, cStart
        ans = []
        direct = [0, 1]
        pos = [rStart, cStart]
        ans.append(pos)
        while len(ans) < rows * cols:
            new_pos = [pos[0] + direct[0], pos[1] + direct[1]]
            if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols:
                ans.append(new_pos)
            if new_pos[0] > max_r:
                max_r = new_pos[0]
                direct = [0, -1]
            elif new_pos[0] < min_r:
                min_r = new_pos[0]
                direct = [0, 1]
            elif new_pos[1] > max_c:
                max_c = new_pos[1]
                direct = [1, 0]
            elif new_pos[1] < min_c:
                min_c = new_pos[1]
                direct = [-1, 0]
            pos = new_pos
        return ans

data = [
5
, 6
, 1
, 4
        ]
r = Solution().spiralMatrixIII(* data)
print(r)