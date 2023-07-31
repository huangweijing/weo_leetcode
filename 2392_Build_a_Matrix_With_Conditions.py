from typing import List

class Graph:
    def __init__(self, vertex_count: int):
        self.adj_list = [[] for _ in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int):
        self.adj_list[v1].append(v2)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adj(self, v) -> list[int]:
        return self.adj_list[v]

    def get_reverse(self):
        rev_graph = Graph(self.vertex_count)
        for from_node in range(self.vertex_count):
            for to_node in self.adj_list[from_node]:
                rev_graph.add_edge(to_node, from_node)
        return rev_graph

class CycleDetect:
    def __init__(self, g: Graph):
        self.g = g
        self.marked = [False] * self.g.vertex_count
        self.stack = [False] * self.g.vertex_count
        self.has_cycle = False
        for v in range(self.g.vertex_count):
            self.dfs(v)

    def dfs(self, v: int):
        self.stack[v] = True
        self.marked[v] = True
        for adj in self.g.get_adj(v):
            if self.has_cycle:
                return
            if not self.marked[adj]:
                self.dfs(adj)
            else:
                if self.stack[adj]:
                    self.has_cycle = True
                    return
        self.stack[v] = False

    def cycle_detected(self) -> bool:
        return self.has_cycle

class TopologicalSort:
    def __init__(self, g: Graph):
        self.g = g
        self.post_order = []
        self.marked = [False] * g.get_vertex_count()
        for v in range(self.g.vertex_count):
            if not self.marked[v]:
                self.deep_first_order(v)

    def get_order(self):
        return self.post_order[::-1]

    def deep_first_order(self, v: int):
        self.marked[v] = True
        for adj in self.g.get_adj(v):
            if not self.marked[adj]:
                self.deep_first_order(adj)
        self.post_order.append(v)


class Solution:
    def buildMatrix(self, k: int,
                    rowConditions: List[List[int]],
                    colConditions: List[List[int]]) -> List[List[int]]:
        row_graph = Graph(k)
        col_graph = Graph(k)
        for cond in rowConditions:
            row_graph.add_edge(cond[0] - 1, cond[1] - 1)
        for cond in colConditions:
            col_graph.add_edge(cond[0] - 1, cond[1] - 1)

        if CycleDetect(row_graph).cycle_detected() or \
            CycleDetect(col_graph).cycle_detected():
            return []

        row_order = TopologicalSort(row_graph).get_order()
        col_order = TopologicalSort(col_graph).get_order()

        ans = [[0] * k for _ in range(k)]
        axis_list = [[0, 0] for _ in range(k)]
        for i, num in enumerate(row_order):
            axis_list[num][0] = i
        for i, num in enumerate(col_order):
            axis_list[num][1] = i

        for i, axis in enumerate(axis_list):
            ans[axis[0]][axis[1]] = i + 1
        return ans

data = [
    3
    , [[1, 2], [2, 3], [3, 1], [2, 3]]
    , [[2, 1]]
]
r = Solution().buildMatrix(* data)
print(r
      )
