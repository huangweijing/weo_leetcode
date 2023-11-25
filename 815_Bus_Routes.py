from typing import List


class Graph:
    def __init__(self, vertex_count: int):
        self.vertex_adj_list = [[] for _ in range(vertex_count)]
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
    def numBusesToDestination(self, routes: List[List[int]]
                              , source: int, target: int) -> int:
        if source == target:
            return 0
        g = Graph(len(routes))
        bus_arr = [set() for _ in routes]
        for i, route in enumerate(routes):
            for stop in route:
                bus_arr[i].add(stop)
                for j in range(i):
                    if stop in bus_arr[j]:
                        g.add_edge(i, j)
        cur_set = set[int]([i for i, route in enumerate(routes) if source in route])
        target_set = set[int]([i for i, route in enumerate(routes) if target in route])
        visited = cur_set.copy()
        ans = 1
        while len(cur_set) > 0:
            new_cur_set = set[int]()
            for v in cur_set:
                if v in target_set:
                    return ans
                adj_list = g.get_adjacent_vertex(v)
                for adj in adj_list:
                    if adj not in visited:
                        visited.add(adj)
                        new_cur_set.add(adj)
            ans += 1
            cur_set = new_cur_set
        return -1

data = [
    [[1, 7], [3, 5]]
    , 5
    , 5
]
r = Solution().numBusesToDestination(* data)
print(r)




