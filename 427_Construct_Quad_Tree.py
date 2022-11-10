from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:

    def make_node_grid(self, grid: list[list[int]]) -> list[list[Node]]:
        new_grid = [[None] * len(grid) for _ in range(len(grid))]
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                new_grid[i][j] = Node(grid[i][j], True, None, None, None, None)
        return new_grid

    def merge_grid(self, grid: list[list[Node]]) -> list[list[Node]]:
        n = len(grid) >> 1
        new_grid = [[None] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                c1, c2, c3, c4 = grid[i * 2][j * 2], grid[i * 2][j * 2 + 1]\
                    , grid[i * 2 + 1][j * 2], grid[i * 2 + 1][j * 2 + 1]
                # print(c1.val, c2.val, c3.val, c4.val)
                new_grid[i][j] = Node(0, True, None, None, None, None)
                if c1.val == c2.val == c3.val == c4.val and \
                    c1.isLeaf == c2.isLeaf == c3.isLeaf == c4.isLeaf == True:
                    new_grid[i][j].val = c1.val
                    new_grid[i][j].isLeaf = True
                else:
                    new_grid[i][j].val = 1
                    new_grid[i][j].isLeaf = False
                    new_grid[i][j].topLeft = c1
                    new_grid[i][j].topRight = c2
                    new_grid[i][j].bottomLeft = c3
                    new_grid[i][j].bottomRight = c4
        return new_grid

    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        node_grid = self.make_node_grid(grid)
        while len(node_grid) > 1:
            node_grid = self.merge_grid(node_grid)
        return node_grid[0][0]

data = [[0,1],[1,0]]
r = Solution().construct(data)
print(r.val)