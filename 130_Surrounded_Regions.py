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
    def v2p(self, v: int, board_width: int) -> (int, int):
        return int(v / board_width), v % board_width

    def p2v(self, i: int, j:int, board_width: int) -> int:
        return i * board_width + j

    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        wuf = WeightedUnionFind(m * n)
        not_sur = list[int]()
        not_sur_root = set[int]()

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    p = self.p2v(i, j, n)
                    if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                        not_sur.append(p)
                    if i > 0 and board[i - 1][j] == "O":
                        wuf.union(p, self.p2v(i - 1, j, n))
                    if j > 0 and board[i][j - 1] == "O":
                        wuf.union(p, self.p2v(i, j - 1, n))
        for p in not_sur:
            not_sur_root.add(wuf.find(p))
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    p = self.p2v(i, j, n)
                    if wuf.find(p) not in not_sur_root:
                        board[i][j] = "X"

board_data = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Solution().solve(board_data)
print(board_data)