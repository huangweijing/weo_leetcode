from typing import List
from collections import deque


class Edge:
    def __init__(self, start: int, end: int, weight: float):
        self.start = start
        self.end = end
        self.weight = weight

class Graph:
    def __init__(self, vertex_count: int):
        self.vertex_adj_list = [[] for x in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int, weight: float):
        self.vertex_adj_list[v1].append(Edge(v1, v2, weight))
        self.vertex_adj_list[v2].append(Edge(v2, v1, weight))
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_edge(self, v) -> list[Edge]:
        return self.vertex_adj_list[v]



class Solution:
    def maxProbability(self, n: int, edges: List[List[int]]
                       , succProb: List[float], start: int, end: int) -> float:
        g = Graph(n)
        for i, edge in enumerate(edges):
            g.add_edge(edge[0], edge[1], succProb[i])
        best_prob = [0] * n
        best_prob[start] = 1
        queue = deque([ start ])
        while len(queue) > 0:
            node = queue.popleft()
            adj_edges = g.get_adjacent_edge(node)
            for edge in adj_edges:
                if best_prob[node] * edge.weight > best_prob[edge.end]:
                    best_prob[edge.end] = best_prob[node] * edge.weight
                    queue.append(edge.end)

        return best_prob[end]

data = [
    3
    , [[0,1],[1,2],[0,2]]
    , [0.5,0.5,0.2]
    , 0
    , 2
]
r = Solution().maxProbability(* data)
print(r)

