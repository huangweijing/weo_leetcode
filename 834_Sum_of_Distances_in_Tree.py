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
    def __init__(self):
        self.g = Graph(0)
        self.parent_dict = dict[int, int]()
        self.node_dist = dict[int, int]()
        self.node_cnt = dict[int, int]()
        self.ans = []

    def make_graph(self, n: int, edges: List[List[int]]):
        self.g = Graph(n)
        for edge in edges:
            self.g.add_edge(edge[0], edge[1])
        self.parent_dict = dict[int, int]()
        self.parent_dict[0] = None
        node_list = [0]
        while len(node_list) > 0:
            node = node_list.pop()
            adj_nodes = self.g.vertex_adj_list[node]
            for adj_node in adj_nodes:
                if adj_node in self.parent_dict:
                    continue
                self.parent_dict[adj_node] = node
                node_list.append(adj_node)

    def calc_graph_info(self, node: int):
        adj_nodes = self.g.get_adjacent_vertex(node)
        cnt, dist = 0, 0
        for adj_node in adj_nodes:
            if adj_node == self.parent_dict[node]:
                continue
            self.calc_graph_info(adj_node)
            cnt += self.node_cnt[adj_node]
            dist += self.node_dist[adj_node]
        self.node_cnt[node] = cnt + 1
        self.node_dist[node] = cnt + dist

    def my_sum(self, node: int):
        parent = self.parent_dict[node]
        if parent is None:
            self.ans[node] = self.node_dist[node]
        else:
            parent_cnt_sum = self.g.vertex_count - self.node_cnt[node]
            self.ans[node] = self.ans[parent] + parent_cnt_sum - self.node_cnt[node]

        adj_nodes = self.g.get_adjacent_vertex(node)
        for adj_node in adj_nodes:
            if adj_node == parent:
                continue
            self.my_sum(adj_node)

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.make_graph(n, edges)
        self.calc_graph_info(0)
        self.ans = [-1] * self.g.vertex_count
        self.ans[0] = self.node_dist[0]
        self.my_sum(0)
        # for node in range(1, n):
        #     self.my_sum(node)
        return self.ans

data = [
    7
    , [[0,1],[0,2],[2,3],[2,4],[2,5], [5,6]]
]
r = Solution().sumOfDistancesInTree(* data)
print(r)






