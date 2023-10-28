from typing import List
from collections import Counter
import math


class Solution:
    def __init__(self):
        self.m, self.n = 3, 3
        self.zero_pos = []
        self.rem_pos = Counter()

    def id(self, r: int, c: int) -> int:
        return r * self.n + c

    def calc_dist(self, id1: int, id2: int) -> int:
        r1, c1 = id1 // self.n, id1 % self.n
        r2, c2 = id2 // self.n, id2 % self.n
        return abs(r1 - r2) + abs(c1 - c2)

    def my_sol(self, i) -> int:
        if i == len(self.zero_pos):
            return 0
        zero = self.zero_pos[i]
        ret = math.inf
        for pos in self.rem_pos.keys():
            if self.rem_pos[pos] > 0:
                self.rem_pos[pos] -= 1
                # print(f"zero={zero}, pos={pos}, dist={self.calc_dist(zero, pos)}")
                ret = min(self.calc_dist(zero, pos) + self.my_sol(i + 1), ret)
                self.rem_pos[pos] += 1
        return ret


    def minimumMoves(self, grid: List[List[int]]) -> int:
        for i, row in enumerate(grid):
            for j, col in enumerate(grid):
                if grid[i][j] == 0:
                    self.zero_pos.append(self.id(i, j))
                elif grid[i][j] > 1:
                    self.rem_pos[self.id(i, j)] += grid[i][j] - 1
        # print(list(map(lambda x: [x // self.n, x % self.m], self.zero_pos)), self.rem_pos)
        ans = self.my_sol(0)
        return ans


data = [[1,3,0],[1,0,0],[1,0,3]]
r = Solution().minimumMoves(data)
print(r)