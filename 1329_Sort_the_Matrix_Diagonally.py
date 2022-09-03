from sortedcontainers import SortedList
from typing import List
from collections import deque

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        for row in range(m):
            col = 0
            q = SortedList()
            for i in range(row, m):
                q.add(mat[i][col])
                col += 1
                if col >= n:
                    break
            q = deque(q)
            col = 0
            for i in range(row, m):
                mat[i][col] = q.popleft()
                col += 1
                if col >= n:
                    break

        for col in range(1, n):
            row = 0
            q = SortedList()
            for i in range(col, n):
                q.add(mat[row][i])
                row += 1
                if row >= m:
                    break
            q = deque(q)
            row = 0
            for i in range(col, n):
                mat[row][i] = q.popleft()
                row += 1
                if row >= m:
                    break
        return mat

data_mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
r = Solution().diagonalSort(data_mat)
print(r)