from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]]
                            , king: List[int]) -> List[List[int]]:
        board_size = 8
        board = [[""] * board_size for _ in range(board_size)]
        for queen in queens:
            board[queen[0]][queen[1]] = "q"
        ans = []
        direction_arr = [[0, 1], [1, 0], [1, 1], [0, -1]
            , [-1, 0], [-1, -1], [1, -1], [-1, 1]]

        for direction in direction_arr:
            pos = king.copy()
            while 0 <= pos[0] < board_size and 0 <= pos[1] < board_size:
                if board[pos[0]][pos[1]] == "q":
                    ans.append(pos)
                    break
                pos = [pos[0] + direction[0], pos[1] + direction[1]]

        return ans