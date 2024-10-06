from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        row, col = 0, 0
        direct = {
            "UP": [-1, 0]
            , "DOWN": [1, 0]
            , "RIGHT": [0, 1]
            , "LEFT": [0, -1]
        }
        for cmd in commands:
            d = direct[cmd]
            row += d[0]
            col += d[1]
        return row * n + col


