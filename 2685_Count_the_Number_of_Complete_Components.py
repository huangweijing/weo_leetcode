from typing import List


class Graph:
    def __init__(self, vertex_count: int):
        self.vertex_adj_list = [[] for x in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int):
        self.vertex_adj_list[v1].append(v2)
        self.vertex_adj_list[v2].append(v1)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_vertex(self, v) -> list[int]:
        return self.vertex_adj_list[v]



class Solution:
    def __init__(self):
        self.g = Graph(0)
        self.visited = []

    def dfs(self, v: int, group: set[int]) -> int:
        if self.visited[v]:
            return 0
        self.visited[v] = True
        group.add(v)
        # print(self.g.get_adjacent_vertex(v))
        adj_list = self.g.get_adjacent_vertex(v)
        cnt = 1
        for adj in adj_list:
            cnt += self.dfs(adj, group)
        return cnt

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        self.g = Graph(n)
        self.visited = [False] * n
        for edge in edges:
            self.g.add_edge(edge[0], edge[1])
        ans = 0
        for i in range(n):
            if not self.visited[i]:
                group = set[int]()
                vertex_cnt = self.dfs(i, group)
                edge_cnt = 0
                for v in group:
                    edge_cnt += len(self.g.vertex_adj_list[v])
                edge_cnt >>= 1
                if vertex_cnt * (vertex_cnt - 1) == edge_cnt * 2:
                    ans += 1
        return ans


data = [
    6
    , [[0, 1], [0, 2], [1, 2], [3, 4]]
]
r = Solution().countCompleteComponents(* data)
print(r)