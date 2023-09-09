from typing import List
import math


class Solution:
    def __init__(self):
        self.mat = []
        self.m = 0
        self.n = 0
        self.ans = math.inf

    def pos2axis(self, pos: int):
        return [pos // self.n, pos % self.n]

    def flip_all(self, did: int, one: int):
        if one >= self.ans:
            return
        if did.bit_count() == self.m * self.n:
            return
        for i in range(self.m * self.n):
            if (did & 1 << i) >> i == 1:
                continue
            did |= 1 << i
            one += self.flip(i)
            if one == 0:
                self.ans = min(self.ans, did.bit_count())
                one += self.flip(i)
                did ^= 1 << i
                return
            self.flip_all(did, one)
            one += self.flip(i)
            did ^= 1 << i

    def flip(self, pos: int) -> int:
        ret = 0
        p = self.pos2axis(pos)
        self.mat[p[0]][p[1]] = abs(1 - self.mat[p[0]][p[1]])
        ret += 1 if self.mat[p[0]][p[1]] == 1 else -1
        if p[0] - 1 >= 0:
            self.mat[p[0] - 1][p[1]] = abs(1 - self.mat[p[0] - 1][p[1]])
            ret += 1 if self.mat[p[0] - 1][p[1]] == 1 else -1
        if p[0] + 1 < self.m:
            self.mat[p[0] + 1][p[1]] = abs(1 - self.mat[p[0] + 1][p[1]])
            ret += 1 if self.mat[p[0] + 1][p[1]] == 1 else -1

        if p[1] - 1 >= 0:
            self.mat[p[0]][p[1] - 1] = abs(1 - self.mat[p[0]][p[1] - 1])
            ret += 1 if self.mat[p[0]][p[1] - 1] == 1 else -1
        if p[1] + 1 < self.n:
            self.mat[p[0]][p[1] + 1] = abs(1 - self.mat[p[0]][p[1] + 1])
            ret += 1 if self.mat[p[0]][p[1] + 1] == 1 else -1
        return ret

    def minFlips(self, mat: List[List[int]]) -> int:
        self.mat = mat
        self.m, self.n = len(self.mat), len(self.mat[0])
        one = sum([sum(row) for row in mat])
        if one == 0:
            return 0
        self.flip_all(0, one)
        if self.ans == math.inf:
            return -1
        return self.ans

mat = [[0,1,0],[1,1,1]]
r = Solution().minFlips(mat)
print(r)
