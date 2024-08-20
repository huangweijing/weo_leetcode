from typing import List
from collections import Counter


class Solution:
    def __init__(self) -> None:
        self.visited = set[int]()
        self.min_res = Counter()
        self.min_res[123450] = 0

    def get_sta(self, board: list[list[int]]) -> int:
        ret = 0
        for row in board:
            for val in row:
                ret = ret * 10 + val
        return ret

    def min_step(self, board: List[List[int]], pos: list[int], visited: set[int]) -> int:
        key = self.get_sta(board)
        # if key in self.min_res:
        #     return self.min_res[key]
        visited.add(key)
        ret = 99999999
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for d in direct:
            new_pos = [pos[0] + d[0], pos[1] + d[1]]
            if 0 <= new_pos[0] < len(board) and 0 <= new_pos[1] < len(board[0]):
                board[new_pos[0]][new_pos[1]], board[pos[0]][pos[1]] = \
                    board[pos[0]][pos[1]], board[new_pos[0]][new_pos[1]]
                if self.get_sta(board) not in visited:
                    ret = min(ret, self.min_step(board, new_pos, visited) + 1)
                board[new_pos[0]][new_pos[1]], board[pos[0]][pos[1]] = \
                    board[pos[0]][pos[1]], board[new_pos[0]][new_pos[1]]
        # print(board, ret, len(self.min_res))
        visited.remove(key)
        if key in self.min_res:
            self.min_res[key] = min(self.min_res[key], ret)
        else:
            self.min_res[key] = ret
        return ret

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        zero_pos = [-1, -1]
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == 0:
                    zero_pos = [i, j]
                    break
        steps = self.min_step(board, zero_pos, set[int]())
        # print(self.min_res)
        # print(self.visited, zero_pos)
        if steps == 99999999:
            return -1
        return steps

print(1^2^3)

data = [[4, 1, 2],[5,0,3]]
r = Solution().slidingPuzzle(data)
print(r)