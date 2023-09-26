import heapq
import math
from typing import List



class Distance:
    def __init__(self, v: int, distance):
        self.v = v
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance


class Edge:
    def __init__(self, v1: int, v2: int, weight: float):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight


class WeightedGraph:
    def __init__(self, vertex_count: int):
        self.vertex_adj_list = [[] for _ in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int, weight: float):
        edge = Edge(v1, v2, weight)
        self.vertex_adj_list[v1].append(edge)
        edge = Edge(v2, v1, weight)
        self.vertex_adj_list[v2].append(edge)
        self.edge_count += 2

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_vertex(self, v) -> list[Edge]:
        return self.vertex_adj_list[v]


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        graph = WeightedGraph(m * n)
        for i, _ in enumerate(heights):
            for j, __ in enumerate(heights):
                if i - 1 >= 0:
                    weight = abs(heights[i][j] - heights[i - 1][j])
                    graph.add_edge(i * n + j, (i - 1) * n + j, weight)
                if i + 1 < m:
                    weight = abs(heights[i][j] - heights[i + 1][j])
                    graph.add_edge(i * n + j, (i + 1) * n + j, weight)
                if j - 1 >= 0:
                    weight = abs(heights[i][j] - heights[i][j - 1])
                    graph.add_edge(i * n + j, i * n + j - 1, weight)
                if j + 1 < n:
                    weight = abs(heights[i][j] - heights[i][j + 1])
                    graph.add_edge(i * n + j, i * n + j + 1, weight)

        s, g = 0, m * n - 1
        dist_arr = [math.inf] * (m * n)
        visited = [False] * (m * n)
        dist_arr[s], visited[s] = 0, True
        node_list = [Distance(0, 0)]
        heapq.heapify(node_list)
        while dist_arr[g] == math.inf:
            print(dist_arr)
            node = heapq.heappop(node_list)
            dist_arr[node.v] = node.distance
            adj_edge_list = graph.get_adjacent_vertex(node.v)
            for adj_edge in adj_edge_list:
                if not visited[adj_edge.v2]:
                    dist = Distance(adj_edge.v2, adj_edge.weight + node.distance)
                    heapq.heappush(node_list, dist)
                    visited[adj_edge.v2] = True
        return dist_arr[g]