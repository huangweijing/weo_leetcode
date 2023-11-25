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


class WeightedGraph:
    def __init__(self, vertex_count: int):
        self.vertex_adj_list = [[] for _ in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int, weight: float):
        edge = Edge(v1, v2, weight)
        self.vertex_adj_list[v1].append(edge)
        # edge = Edge(v2, v1, weight)
        # self.vertex_adj_list[v2].append(edge)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_vertex(self, v) -> list[Edge]:
        return self.vertex_adj_list[v]



class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.g = WeightedGraph(n)
        for edge in edges:
            self.g.add_edge(*edge)

    def addEdge(self, edge: List[int]) -> None:
        self.g.add_edge(*edge)

    def shortestPath(self, node1: int, node2: int) -> int:
        s, g = node1, node2
        dist_arr = [math.inf] * self.n
        visited = [False] * self.n
        dist_arr[node1], visited[node1] = 0, False
        node_list = [Distance(node1, 0)]
        heapq.heapify(node_list)
        while dist_arr[g] == math.inf and len(node_list) > 0:
            node = heapq.heappop(node_list)
            if visited[node.v]:
                continue
            visited[node.v] = True
            dist_arr[node.v] = min(node.distance, dist_arr[node.v])
            adj_edge_list = self.g.get_adjacent_vertex(node.v)
            for adj_edge in adj_edge_list:
                # if not visited[adj_edge.v2]:
                dist = Distance(adj_edge.v2, adj_edge.weight + node.distance)
                heapq.heappush(node_list, dist)
                # visited[adj_edge.v2] = True
            # print(dist_arr, list(map(lambda x: [x.v, x.distance],  node_list)))
        if dist_arr[node2] == math.inf:
            return -1
        return dist_arr[node2]

# data = [
#     4
#     , [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]
# ]
# g = Graph(* data)
# print(g.shortestPath(3, 2))


data = [
    ["Graph","shortestPath","addEdge","addEdge","addEdge","shortestPath","shortestPath","shortestPath","addEdge","shortestPath","addEdge","shortestPath","shortestPath","addEdge","addEdge","shortestPath","addEdge","addEdge","addEdge","addEdge","addEdge","shortestPath","shortestPath","shortestPath","shortestPath","shortestPath","shortestPath","shortestPath","shortestPath","shortestPath","shortestPath","shortestPath","shortestPath","shortestPath","shortestPath","shortestPath"]
    , [[4,[]],[2,2],[[0,3,745857]],[[1,3,432074]],[[0,2,103840]],[0,2],[0,1],[1,0],[[2,0,100674]],[0,2],[[1,2,977334]],[2,1],[0,0],[[0,1,686587]],[[3,1,65074]],[2,0],[[2,3,871421]],[[3,0,19073]],[[1,0,751462]],[[2,1,12018]],[[3,2,989255]],[1,3],[2,0],[3,1],[3,2],[2,3],[2,2],[3,3],[2,1],[3,0],[3,3],[1,0],[0,3],[1,2],[3,0],[2,2]]
]
ssa = Graph(*data[1][0])
result = []
for idx, command in enumerate(zip(data[0], data[1])):
    if idx == 0:
        continue
    ret = getattr(ssa, command[0])(* command[1])
    print(command[0], command[1], ret)
    result.append(ret)
print(result)