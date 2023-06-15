from typing import List
from functools import cache

class Edge:
    def __init__(self, v1: str, v2: str, weight: float):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

class Graph:
    def __init__(self, vertex_count: int):
        self.vertex_adj_dict = dict[str, dict[str, Edge]]()
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: str, v2: str, weight: float):
        if v1 in self.vertex_adj_dict and v2 in self.vertex_adj_dict\
                and self.calc_path("", v1, v2) != -1:
            return
        if v1 not in self.vertex_adj_dict:
            self.vertex_adj_dict[v1] = dict[str, Edge]()
        if v2 not in self.vertex_adj_dict:
            self.vertex_adj_dict[v2] = dict[str, Edge]()
        self.vertex_adj_dict[v1][v2] = Edge(v1, v2, weight)
        self.vertex_adj_dict[v2][v1] = Edge(v2, v1, 1 / weight)
        # self.vertex_adj_list[v1].append(v2)
        # self.vertex_adj_list[v2].append(v1)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_vertex(self, v) -> list[int]:
        return self.vertex_adj_list[v]

    @cache
    def calc_path(self, ent: str, v1: str, v2: str) -> float:
        adj_dict = self.vertex_adj_dict[v1]
        for adj, w in adj_dict.items():
            if adj == ent:
                continue
            if adj == v2:
                return w.weight
            path_val = self.calc_path(v1, adj, v2)
            if path_val != -1:
                return w.weight * path_val
        return -1

class Solution:
    def __init__(self):
        self.var_table = dict[int, str]()

    def add_val(self, var: str, val: float):
        if var not in self.var_table:
            self.var_table[var] = val

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = Graph(40)
        for i in range(len(equations)):
            eq = equations[i]
            val = values[i]
            g.add_edge(eq[0], eq[1], val)

        ans = []
        for query in queries:
            if query[0] in g.vertex_adj_dict and query[1] in g.vertex_adj_dict:
                if query[0] == query[1]:
                    ans.append(1)
                else:
                    path = g.calc_path("", query[0], query[1])
                    ans.append(path)
            else:
                ans.append(-1)

        return ans


data = [
    [["a", "b"], ["b", "c"], ["a", "c"], ["d", "e"]]
    , [2.0, 3.0, 6.0, 1.0]
    , [["a", "c"], ["b", "c"], ["a", "e"], ["a", "a"], ["x", "x"], ["a", "d"]]
]
r = Solution().calcEquation(* data)
print(r)