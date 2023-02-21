from typing import List
from collections import deque


class Graph:
    def __init__(self, vertex_count: int):
        self.out_vertex_adj_set = [set[int]() for _ in range(vertex_count)]
        self.in_vertex_adj_set = [set[int]() for _ in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int):
        self.out_vertex_adj_set[v1].add(v2)
        self.in_vertex_adj_set[v2].add(v1)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_out_adjacent_vertex(self, v) -> set[int]:
        return self.out_vertex_adj_set[v]

    def get_in_adjacent_vertex(self, v) -> set[int]:
        return self.in_vertex_adj_set[v]


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = Graph(n)
        # print(edges)
        prev_set = [set[int]() for _ in range(n)]
        ans = [list[int]() for _ in range(n)]
        visited = [False] * n
        edges.sort(key=lambda x: x[0])
        for edge in edges:
            g.add_edge(edge[0], edge[1])

        node_queue = deque()
        for node in range(n):
            # print(node, g.in_vertex_adj_set[node])
            if len(g.in_vertex_adj_set[node]) == 0:
                visited[node] = True
                node_queue.append(node)

        while len(node_queue) > 0:
            node = node_queue.popleft()
            in_set = g.get_in_adjacent_vertex(node)
            node_in_set = in_set.copy()
            for v in in_set:
                node_in_set.update(prev_set[v])
            prev_set[node] = node_in_set

            out_node_set = g.get_out_adjacent_vertex(node)
            for v in out_node_set:
                if visited[v]:
                    continue
                prev_not_vis = [1 for x in g.get_in_adjacent_vertex(v) if not visited[x]]
                if len(prev_not_vis) == 0:
                    visited[v] = True
                    node_queue.append(v)

        for i in range(n):
            ans[i] = list[int](prev_set[i])
            ans[i].sort()

        return ans

data = [
    6
    , [[0,3],[5,0],[2,3],[4,3],[5,3],[1,3],[2,5],[0,1],[4,5],[4,2],[4,0],[2,1],[5,1]]
]
r = Solution().getAncestors(* data)
print(r)

# a = set[int]([1, 2, 3, 4 ,4])
# a = a.union(list(range(10)))
# print(a)