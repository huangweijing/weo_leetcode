from typing import List

class Solution:

    def __init__(self):
        self.solution: List[List[str]] = []
        self.solution_set = set[str]()

    def totalNQueens(self, n: int) -> int:
        r = self.solveNQueens(n)
        return len(r)

    @classmethod
    def init_board(cls, n: int):
        board = [["."] * n for i in range(n)]
        return board

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = Solution.init_board(n)
        self.solve(board, 0)
        return self.solution

    def solve(self, board: List[List[str]], row: int):
        if row == len(board):
            # Solution.print_board(board)
            result = Solution.format_result(board)
            set_key = "".join(result)
            if set_key not in self.solution_set:
                self.solution_set.add(set_key)
                self.solution.append(result)
            return

        for col in range(len(board)):
            if not Solution.check_conflict(board, row, col):
                board[row][col] = "Q"
                self.solve(board, row + 1)
                board[row][col] = "."

    @classmethod
    def format_result(cls, board: List[List[str]]) -> List[str]:
        result = []
        for row in range(len(board)):
            s = "".join(board[row])
            result.append(s)
        return result

    @classmethod
    def print_board(cls, board: List[List[str]]):
        for i in range(len(board)):
            print(board[i])

    @classmethod
    def print_board_str(cls, board: List[str]):
        for row in range(len(board)):
            print(board[row])
        print()

    @classmethod
    def check_conflict(cls, board: List[List[str]], row: int, col: int):
        for idx in range(len(board)):
            if board[idx][col] == "Q":
                return True
            if board[row][idx] == "Q":
                return True

        idx = col - 1
        idx2 = row - 1

        while idx >= 0 and idx2 >= 0:
            if board[idx2][idx] == "Q":
                return True
            idx -= 1
            idx2 -= 1

        idx = col - 1
        idx2 = row + 1
        while idx >= 0 and idx2 < len(board):
            if board[idx2][idx] == "Q":
                return True
            idx -= 1
            idx2 += 1

        idx = col + 1
        idx2 = row - 1
        while idx < len(board) and idx2 >= 0:
            if board[idx2][idx] == "Q":
                return True
            idx += 1
            idx2 -= 1

        idx = col + 1
        idx2 = row + 1
        while idx < len(board) and idx2 < len(board):
            if board[idx2][idx] == "Q":
                return True
            idx += 1
            idx2 += 1

        return False