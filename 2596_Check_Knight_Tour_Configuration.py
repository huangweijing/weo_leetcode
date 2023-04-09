from typing import List

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        pos_dict = dict[int, list[int]]()
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                pos_dict[val] = [i, j]
        if pos_dict[0] != [0, 0]:
            return False
        for i in range(len(pos_dict) - 1):
            pos = pos_dict[i]
            next_pos = pos_dict[i + 1]
            vec = [abs(next_pos[0] - pos[0]), abs(next_pos[1] - pos[1])]
            if not (vec == [2, 1] or vec == [1, 2]):
                return False
        return True

