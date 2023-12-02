from typing import List
import heapq
import math


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

    def __str__(self) -> str:
        return f"<{self.v1},{self.v2},{self.weight}>"


class WeightedGraph:
    def __init__(self, vertex_count: int):
        self.vertex_adj_list = [dict[int, Edge]() for _ in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int, weight: float):
        if v2 in self.vertex_adj_list[v1]:
            if weight < self.vertex_adj_list[v1][v2].weight:
                self.vertex_adj_list[v1][v2].weight = weight
        else:
            edge = Edge(v1, v2, weight)
            self.vertex_adj_list[v1][v2] = edge
            self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_vertex(self, v):
        return self.vertex_adj_list[v].values()

    def shortestPath(self, node1: int, node2: int) -> int:
        s, g = node1, node2
        dist_arr = [math.inf] * self.vertex_count
        visited = [False] * self.vertex_count
        dist_arr[node1], visited[node1] = 0, False
        node_list = [Distance(node1, 0)]
        heapq.heapify(node_list)
        while dist_arr[g] == math.inf and len(node_list) > 0:
            node = heapq.heappop(node_list)
            if visited[node.v]:
                continue
            visited[node.v] = True
            dist_arr[node.v] = min(node.distance, dist_arr[node.v])
            adj_edge_list = self.get_adjacent_vertex(node.v)
            for adj_edge in adj_edge_list:
                # if not visited[adj_edge.v2]:
                dist = Distance(adj_edge.v2, adj_edge.weight + node.distance)
                heapq.heappush(node_list, dist)
                # visited[adj_edge.v2] = True
            # print(dist_arr, list(map(lambda x: [x.v, x.distance],  node_list)))
            # print(dist_arr)
        if dist_arr[node2] == math.inf:
            return -1
        return dist_arr[node2]

class Solution:
    def __init__(self):
        self.max_cnt = 100001
        self.key_id = dict[int, int]()
        self.id_key = dict[int, int]()

    def get_id(self, x: int, y: int) -> int:
        key = x * self.max_cnt + y
        if key in self.key_id:
            return self.key_id[key]
        road_id = len(self.key_id)
        self.id_key[road_id] = key
        self.key_id[key] = road_id
        return road_id

    def minimumCost(self, start: List[int]
                    , target: List[int], specialRoads: List[List[int]]) -> int:
        s_id = self.get_id(start[0], start[1])
        t_id = self.get_id(target[0], target[1])
        wg = WeightedGraph(500)
        for road in specialRoads:
            r1_id = self.get_id(road[0], road[1])
            r2_id = self.get_id(road[2], road[3])
            wg.add_edge(r1_id, r2_id, road[4])
        for id1, key1 in self.id_key.items():
            x1 = key1 // self.max_cnt
            y1 = key1 % self.max_cnt
            for id2, key2 in self.id_key.items():
                if id1 == id2:
                    continue
                x2 = key2 // self.max_cnt
                y2 = key2 % self.max_cnt
                wg.add_edge(id1, id2, abs(x2 - x1) + abs(y2 - y1))

        # for i, adj_list in enumerate(wg.vertex_adj_list):
        #     # print(i, list(map(str, adj_list)))
        #     print(i, list(map(str, adj_list.values())))
        # print(len(self.key_id))
        ans = wg.shortestPath(s_id, t_id)
        return ans


data = [
    [1, 1]
    , [100000, 100000]
    , [[1, 1, 100000, 99999, 19999]]
]
r = Solution().minimumCost(* data)
print(r)

