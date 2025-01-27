from typing import List
from collections import defaultdict

class Solution:
    def __init__(self) -> None:
        self.grid = []

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        self.grid = grid
        m, n = len(grid), len(grid[0])
        group = dict[int, int]()
        group_nodes = defaultdict(lambda: set[int]())
        group_border = defaultdict(lambda: set[int]())
        visited = set[int]()
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                node = i * n + j
                if val == 1 or node in visited:
                    continue
                group_id = len(group)
                next_set = set[int]([node])
                while len(next_set) > 0:
                    cur = next_set.pop()
                    visited.add(cur)
                    group[cur] = group_id
                    group_nodes[group_id].add(cur)
                    row_idx, col_idx = cur // n, cur % n
                    for direct in direction:
                        new_row_idx, new_col_idx = row_idx + direct[0], col_idx + direct[1]
                        if 0 <= new_row_idx < m and 0 <= new_col_idx < n:
                            if grid[new_row_idx][new_col_idx] == 0:
                                if new_row_idx * n + new_col_idx not in visited:
                                    next_set.add(new_row_idx * n + new_col_idx)
                            else:
                                group_border[group_id].add(new_row_idx * n + new_col_idx)
                    print(next_set, visited, group_border)
        print(group_nodes)

        
data = [[0,1,1],[1,1,0],[1,1,0]]
r = Solution().minimumObstacles(data)
print(r)