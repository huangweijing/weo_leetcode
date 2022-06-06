from typing import List

class Solution:
    def __init__(self):
        self.full_set = set(list(["1", "2", "3", "4", "5", "6", "7", "8", "9"]))
        self.has_found_result = False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        pos = self.find_next_pos(board, 0, 0)
        self.solve(board, pos[0], pos[1])

    def solve(self, board: List[List[str]], row: int, col: int):
        # self.print_board(board)
        # print(row, col)
        if board[row][col] != ".":
            return
        if row == len(board):
            # print(board)
            return
        valid_set = self.get_valid_selection(board, row, col)
        # print(valid_set, row, col)
        if len(valid_set) == 0:
            return
        for num in valid_set:
            board[row][col] = num
            next_pos = self.find_next_pos(board, row, col)
            if next_pos is None:
                self.has_found_result = True
                return
            else:
                self.solve(board, next_pos[0], next_pos[1])
                if self.has_found_result:
                    return
                board[row][col] = "."

    def find_next_pos(self, board: List[List[str]], row: int, col: int):
        len_board = len(board)
        idx = row * len_board + col
        if idx > len_board ** 2 - 1:
            return None
        # print(idx, int(idx / len_board), idx % len_board)
        while idx <= len_board ** 2 - 1 and board[int(idx / len_board)][idx % len_board] != ".":
            idx = idx + 1
        if idx > len_board ** 2 - 1:
            return None
        return [int(idx / len_board), idx % len_board]

    def print_board(self, board: List[List[str]]):
        for row in board:
            print(row)

    def get_valid_selection(self, board:List[List[str]], row_idx:int, col_idx: int):
        num_set = set[str]()
        for row in range(len(board)):
            if "1" <= board[row][col_idx] <= "9":
                num_set.add(board[row][col_idx])

        for col in range(len(board)):
            if "1" <= board[row_idx][col] <= "9":
                num_set.add(board[row_idx][col])

        left_top_idx = int(row_idx / 3) * 3 + int(col_idx / 3)
        left_top_list = [
            [0, 0], [0, 3], [0, 6]
            , [3, 0], [3, 3], [3, 6]
            , [6, 0], [6, 3], [6, 6]
        ]
        left_top = left_top_list[left_top_idx]
        for row_offset in range(3):
            for col_offset in range(3):
                row = row_offset + left_top[0]
                col = col_offset + left_top[1]
                if "1" <= board[row][col] <= "9":
                    num_set.add(board[row][col])

        return self.full_set.difference(num_set)


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
b = [[".", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."],
     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

b2 = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
      ["7", ".", ".", ".", ".", ".", ".", ".", "."],
      [".", "2", ".", "1", ".", "9", ".", ".", "."],
      [".", ".", "7", ".", ".", ".", "2", "4", "."],
      [".", "6", "4", ".", "1", ".", "5", "9", "."],
      [".", "9", "8", ".", ".", ".", "3", ".", "."],
      [".", ".", ".", "8", ".", "3", ".", "2", "."],
      [".", ".", ".", ".", ".", ".", ".", ".", "6"],
      [".", ".", ".", "2", "7", "5", "9", ".", "."]]

# s = sol.get_valid_selection(b, 0, 2)
pos = sol.find_next_pos(b2, 0, 0)
print(pos)
sol.solve(b2, pos[0], pos[1])
sol.print_board(b2)
# print(r)
# set1 = set(list([0, 1, 2]))
# set2 = set(list([0, 1, 2, 3, 4]))
# print(list(set2.difference(set1)))