from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        new_board = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                live_cell = 0
                # live_cell += board[i][j]
                if j > 0:
                    live_cell += board[i][j - 1]
                if j < n - 1:
                    live_cell += board[i][j + 1]
                if i > 0:
                    live_cell += board[i - 1][j]
                    if j > 0:
                        live_cell += board[i - 1][j - 1]
                    if j < n - 1:
                        live_cell += board[i - 1][j + 1]
                if i < m - 1:
                    live_cell += board[i + 1][j]
                    if j > 0:
                        live_cell += board[i + 1][j - 1]
                    if j < n - 1:
                        live_cell += board[i + 1][j + 1]
                # print(i, j, live_cell)
                if board[i][j] == 0:
                    if live_cell == 3:
                        new_board[i][j] = 1
                elif board[i][j] == 1:
                    if live_cell in (2, 3):
                        new_board[i][j] = 1
        for i in range(m):
            board[i] = new_board[i]

data = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Solution().gameOfLife(data)
print(data)


