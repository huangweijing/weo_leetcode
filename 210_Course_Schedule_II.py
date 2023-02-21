from typing import List
from collections import deque


class Graph:
    def __init__(self, vertex_count: int):
        self.vertex_adj_list = [[] for _ in range(vertex_count)]
        self.vertex_rev_adj_list = [[] for _ in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int):
        self.vertex_adj_list[v1].append(v2)
        self.vertex_rev_adj_list[v2].append(v1)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_vertex(self, v) -> list[int]:
        return self.vertex_adj_list[v]

    def get_rev_adjacent_vertex(self, v) -> list[int]:
        return self.vertex_rev_adj_list[v]


class Solution:
    def __init__(self):
        self.g = Graph(0)
        self.has_loop = []
        self.path = set[int]()
        self.visited = []

    def dfs_check_loop(self, node: int) -> bool:
        if self.has_loop[node] is not None:
            return self.has_loop[node]
        if node in self.path:
            self.has_loop[node] = True
            return True
        self.path.add(node)
        adj_list = self.g.get_adjacent_vertex(node)
        for adj_node in adj_list:
            if self.dfs_check_loop(adj_node):
                self.has_loop[node] = True
                return True
        self.path.remove(node)
        self.has_loop[node] = False
        return False

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = Graph(numCourses)
        self.has_loop = [None] * numCourses
        self.g = g
        for conn in prerequisites:
            g.add_edge(conn[0], conn[1])
        for node in range(numCourses):
            if self.dfs_check_loop(node):
                return []

        ans = []
        node_queue = deque([v for v in range(self.g.vertex_count) if len(self.g.vertex_adj_list[v]) == 0])
        visited = set[int]()
        to_visit = set[int](node_queue)
        # print(node_queue)
        while len(node_queue) > 0:
            # print(node_queue, ans)
            node = node_queue.popleft()
            pre_list = self.g.get_adjacent_vertex(node)
            should_go = True
            for pre in pre_list:
                if pre not in visited:
                    should_go = False
                    break
            if not should_go:
                node_queue.append(node)
                continue
            visited.add(node)
            to_visit.remove(node)
            ans.append(node)
            adj_list = self.g.get_rev_adjacent_vertex(node)
            for adj in adj_list:
                if adj not in to_visit and adj not in visited:
                    node_queue.append(adj)
                    to_visit.add(adj)
        return ans

data = [
    3,
    [[0,1],[0,2],[1,2]]
]
r = Solution().findOrder(* data)
print(r)