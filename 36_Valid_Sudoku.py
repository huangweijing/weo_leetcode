from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(len(board)):
            num_set = set[str]()
            for col in range(len(board)):
                if not ("0" <= board[row][col] <= "9"
                        or board[row][col] == "."):
                    return False
                if board[row][col] != "." and board[row][col] in num_set:
                    return False
                num_set.add(board[row][col])


        for col in range(len(board)):
            num_set = set[str]()
            for row in range(len(board)):
                if board[row][col] != "." and board[row][col] in num_set:
                    return False
                num_set.add(board[row][col])
        left_top_list = [
            [0, 0], [0, 3], [0, 6]
            , [3, 0], [3, 3], [3, 6]
            , [6, 0], [6, 3], [6, 6]
        ]

        for left_top in left_top_list:
            num_set = set[str]()
            for row_offset in range(3):
                for col_offset in range(3):
                    row = row_offset + left_top[0]
                    col = col_offset + left_top[1]
                    if board[row][col] != "." and board[row][col] in num_set:
                        return False
                    num_set.add(board[row][col])

        return True

sol = Solution()
r = sol.isValidSudoku(
    [["7", ".", ".", ".", "4", ".", ".", ".", "."],
     [".", ".", ".", "8", "6", "5", ".", ".", "."],
     [".", "1", ".", "2", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", "9", ".", ".", "."],
     [".", ".", ".", ".", "5", ".", "5", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", "2", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "."]])
print(r)
