from typing import List
from collections import Counter


class Solution:
    goal = 123450

    def __init__(self) -> None:
        pass

    def get_sta(self, board: list[list[int]]) -> int:
        ret = 0
        for row in board:
            for val in row:
                ret = ret * 10 + val
        return ret

    def min_step(self, start_board: List[List[int]], start_pos: list[int]) -> int:
        key = self.get_sta(start_board)
        next_step = [[start_board, start_pos]]
        visited = set[int]([key])
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        step = 0
        while len(next_step) > 0:
            new_next_step = []
            while len(next_step) > 0:
                next_data = next_step.pop()
                board, pos = next_data[0], next_data[1]
                if self.get_sta(board) == self.goal:
                    return step
                for d in direct:
                    new_pos = [pos[0] + d[0], pos[1] + d[1]]
                    if 0 <= new_pos[0] < len(board) and 0 <= new_pos[1] < len(board[0]):
                        next_board = [row.copy() for row in board]
                        next_board[new_pos[0]][new_pos[1]], next_board[pos[0]][pos[1]] = \
                            next_board[pos[0]][pos[1]], next_board[new_pos[0]][new_pos[1]]
                        new_key = self.get_sta(next_board)
                        if new_key not in visited:
                            visited.add(new_key)
                            new_next_step.append([next_board, new_pos])
            step += 1
            next_step = new_next_step
        return -1


    def slidingPuzzle(self, board: List[List[int]]) -> int:
        zero_pos = [-1, -1]
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == 0:
                    zero_pos = [i, j]
                    break
        steps = self.min_step(board, zero_pos)
        return steps

data = [[4, 1, 2],[5,0,3]]
r = Solution().slidingPuzzle(data)
print(r)