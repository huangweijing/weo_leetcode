from typing import List


class Graph:
    def __init__(self, vertex_count: int):
        self.vertex_adj_list = [set[int]() for x in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int):
        self.vertex_adj_list[v1].add(v2)
        self.vertex_adj_list[v2].add(v1)
        self.edge_count += 1

    def del_edge(self, v1: int, v2: int):
        self.vertex_adj_list[v1].remove(v2)
        self.vertex_adj_list[v2].remove(v1)
        self.edge_count -= 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_vertex(self, v) -> set[int]:
        return self.vertex_adj_list[v]


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        g = Graph(n)
        for edge in edges:
            g.add_edge(edge[0], edge[1])
        node_set = set[int]()
        for v in range(n):
            if len(g.vertex_adj_list[v]) == 1:
                node_set.add(v)

        ans = []
        while len(node_set) > 0:
            # print(node_set)
            ans = list(node_set.copy())
            new_node_set = set[int]()
            while len(node_set) > 0:
                node = node_set.pop()
                adj_set = g.vertex_adj_list[node].copy()
                # print(node, adj_set)
                for adj in adj_set:
                    g.del_edge(node, adj)
                    if len(g.vertex_adj_list[adj]) == 1:
                        new_node_set.add(adj)
            node_set = new_node_set
        return ans

data = [
    4
    ,[[1,0],[1,2],[1,3]]
]
r = Solution().findMinHeightTrees(* data)
print(r)


