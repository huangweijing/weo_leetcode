from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = [0] * m
        col = [0] * n
        for index in indices:
            row[index[0]] += 1
            col[index[1]] += 1
        result = 0
        for i in range(m):
            for j in range(n):
                if (row[i] + col[j]) & 1 == 1:
                    result += 1
        return result

