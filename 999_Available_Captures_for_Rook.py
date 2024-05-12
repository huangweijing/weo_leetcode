from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_pos = (0, 0)
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == "R":
                    rook_pos = (i, j)
                    break
        ans = 0
        for i in range(rook_pos[0] - 1, -1, -1):
            if board[i][rook_pos[1]] == "p":
                ans += 1
                break
            elif board[i][rook_pos[1]] == ".":
                continue
            else:
                break
        for i in range(rook_pos[0] + 1, len(board)):
            if board[i][rook_pos[1]] == "p":
                ans += 1
                break
            elif board[i][rook_pos[1]] == ".":
                continue
            else:
                break
        for i in range(rook_pos[1] - 1, -1, -1):
            if board[rook_pos[0]][i] == "p":
                ans += 1
                break
            elif board[rook_pos[0]][i] == ".":
                continue
            else:
                break
        for i in range(rook_pos[1] + 1, len(board)):
            if board[rook_pos[0]][i] == "p":
                ans += 1
                break
            elif board[rook_pos[0]][i] == ".":
                continue
            else:
                break
        return ans

data = [[".",".",".",".",".",".",".","."]
       ,[".",".",".","p",".",".",".","."]
       ,[".",".",".","R",".",".",".","p"]
       ,[".",".",".",".",".",".",".","."]
       ,[".",".",".",".",".",".",".","."]
       ,[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
r = Solution().numRookCaptures(data)
print(r)
