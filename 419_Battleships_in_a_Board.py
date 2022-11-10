from typing import List

class WeightedUnionFind:

    def __init__(self, size):
        self.node = [i for i in range(size)]
        self.size = [1] * size
        self.count = size
        pass

    def find(self, p: int):
        while self.node[p] != p:
            p = self.node[p]
        return p

    def union(self, p: int, q: int):
        p = self.find(p)
        q = self.find(q)
        if p == q:
            return
        if self.size[p] < self.size[q]:
            self.node[p] = q
            self.size[q] = self.size[q] + self.size[p]
        else:
            self.node[q] = p
            self.size[p] = self.size[q] + self.size[p]
        self.count -= 1

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        wuf = WeightedUnionFind(m * n)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    if i > 0 and board[i - 1][j] == "X":
                        wuf.union(n * i + j, n * (i - 1) + j)
                    if j > 0 and board[i][j - 1] == "X":
                        wuf.union(n * i + j, n * i + (j - 1))
        ans = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    ans.add(wuf.find(n * i + j))
        return len(ans)


