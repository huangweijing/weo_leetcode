import math
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
    def minimumFuelCost(self, roads: List[List[int]]
                        , seats: int) -> int:
        n = len(roads) + 1
        g = Graph(n)
        for road in roads:
            g.add_edge(road[0], road[1])
        # print(g.vertex_adj_list)

        layer_list = []
        cur_layer = [0]
        parent = [-1] * n
        while len(cur_layer) > 0:
            layer_list.append(cur_layer.copy())
            new_layer = []
            while len(cur_layer) > 0:
                node = cur_layer.pop()
                adj_node_list = g.get_adjacent_vertex(node)
                for adj in adj_node_list:
                    if adj != parent[node]:
                        new_layer.append(adj)
                        parent[adj] = node
            cur_layer = new_layer

        ans = 0
        people_cnt = [1] * n
        while len(layer_list) > 1:
            layer = layer_list.pop()
            for node in layer:
                par = parent[node]
                people_cnt[par] += people_cnt[node]
                ans += math.ceil(people_cnt[node] / seats)

        return ans

data = [
    [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
    , 2
]
r = Solution().minimumFuelCost(* data)
print(r)
