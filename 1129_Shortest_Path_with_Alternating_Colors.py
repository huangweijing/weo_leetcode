from typing import List


class Graph:
    def __init__(self, vertex_count: int):
        # self.vertex_adj_list = [[] for x in range(vertex_count)]
        self.blue_adj_list = [[] for x in range(vertex_count)]
        self.red_adj_list = [[] for x in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_blue_edge(self, v1: int, v2: int):
        self.blue_adj_list[v1].append(v2)
        self.edge_count += 1

    def add_red_edge(self, v1: int, v2: int):
        self.red_adj_list[v1].append(v2)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_red_adj_vertex(self, v) -> list[int]:
        return self.red_adj_list[v]

    def get_blue_adj_vertex(self, v) -> list[int]:
        return self.blue_adj_list[v]


class Solution:
    def shortestAlternatingPaths(self, n: int
                                 , redEdges: List[List[int]]
                                 , blueEdges: List[List[int]]) -> List[int]:
        g = Graph(n)
        for red_edge in redEdges:
            g.add_red_edge(red_edge[0], red_edge[1])
        for blue_edge in blueEdges:
            g.add_blue_edge(blue_edge[0], blue_edge[1])

        from_red_visited = [-1 for _ in range(n)]
        from_blue_visited = [-1 for _ in range(n)]

        from_blue_visited[0], from_red_visited[0] = 0, 0
        red_node_list, blue_node_list = [0], [0]
        path_len = 0
        while len(red_node_list) > 0 or len(blue_node_list) > 0:
            new_red_node_list, new_blue_node_list = [], []
            path_len += 1
            while len(red_node_list) > 0:
                rn = red_node_list.pop()
                for adj in g.get_blue_adj_vertex(rn):
                    if from_blue_visited[adj] == -1:
                        from_blue_visited[adj] = path_len
                        new_blue_node_list.append(adj)

            while len(blue_node_list) > 0:
                rn = blue_node_list.pop()
                for adj in g.get_red_adj_vertex(rn):
                    if from_red_visited[adj] == -1:
                        from_red_visited[adj] = path_len
                        new_red_node_list.append(adj)
            red_node_list = new_red_node_list
            blue_node_list = new_blue_node_list
        ans = []
        for red, blue in zip(from_red_visited, from_blue_visited):
            if red == -1:
                ans.append(blue)
            elif blue == -1:
                ans.append(red)
            else:
                ans.append(min(red, blue))
        # print(from_red_visited)
        # print(from_blue_visited)
        return ans

data = [
    5
    , [[0,1],[1,2],[2,3],[3,4]]
    , [[1,2],[2,3],[3,1]]
]
r = Solution().shortestAlternatingPaths(* data)
print(r)

