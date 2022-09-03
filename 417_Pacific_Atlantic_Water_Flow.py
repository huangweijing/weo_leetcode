from typing import List

class DirectedGraphList:
    def __init__(self, vertex_count: int):
        self.vertex_adj_list = [[] for x in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int):
        self.vertex_adj_list[v1].append(v2)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_vertex(self, v) -> list[int]:
        return self.vertex_adj_list[v]

class Solution:
    def __init__(self):
        self.visited = set[int]()
        self.ocean = dict[int, int]() # 0: nothing, 1: atlantic, 2: pacific, 3: both

    def key_to_pos(self, key: int) -> (int, int):
        return int(key / 200), key % 200

    def pos_to_key(self, r: int, c: int) -> int:
        return r * 200 + c

    def dfs(self, g: DirectedGraphList, pos_key: int, ocean: int):
        visited = set[int]()
        s = list[int]()
        s.append(pos_key)
        visited.add(pos_key)
        while len(s) > 0:
            node = s.pop()
            self.ocean[node] = self.ocean.get(node, 0) | ocean
            adj_list = g.get_adjacent_vertex(node)
            for adj in adj_list:
                if adj in visited:
                    continue
                visited.add(adj)
                s.append(adj)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        g = DirectedGraphList(200 * 200)
        for r in range(m):
            for c in range(n):
                key = self.pos_to_key(r, c)
                key_up = self.pos_to_key(r - 1, c)
                key_left = self.pos_to_key(r, c - 1)
                key_down = self.pos_to_key(r + 1, c)
                key_right = self.pos_to_key(r, c + 1)
                if c > 0 and heights[r][c] <= heights[r][c - 1]:
                    g.add_edge(key, key_left)
                if c < n - 1 and heights[r][c] <= heights[r][c + 1]:
                    g.add_edge(key, key_right)
                if r > 0 and heights[r][c] <= heights[r - 1][c]:
                    g.add_edge(key, key_up)
                if r < m - 1 and heights[r][c] <= heights[r + 1][c]:
                    g.add_edge(key, key_down)

        for i in range(m):
            self.dfs(g, self.pos_to_key(i, 0), 2)

        for i in range(1, n):
            self.dfs(g, self.pos_to_key(0, i), 2)

        for i in range(m):
            self.dfs(g, self.pos_to_key(i, n - 1), 1)

        for i in range(0, n - 1):
            self.dfs(g, self.pos_to_key(m - 1, i), 1)

        result = []
        for row in range(m):
            for col in range(n):
                key = self.pos_to_key(row, col)
                if self.ocean.get(key, 0) == 3:
                    result.append([row, col])
        return result

data_heights = [[3,3,3,3,3,3],[3,0,3,3,0,3],[3,3,3,3,3,3]]
r = Solution().pacificAtlantic(data_heights)
print(r)