from typing import List


class Graph:
    def __init__(self, vertex_count: int, node_name: list[int]):
        self.adj_list = [[] for _ in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count
        self.node_map = dict[int, int]()
        if node_name is not None:
            self.node_name = node_name
            self.node_map = {node_name[i]: i for i in range(vertex_count)}
        else:
            self.node_name = list(range(vertex_count))
            self.node_map = {i : i for i in range(vertex_count)}

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
        rev_graph = Graph(self.vertex_count, self.node_name)
        for from_node in range(self.vertex_count):
            for to_node in self.adj_list[from_node]:
                rev_graph.add_edge(to_node, from_node)
        return rev_graph

    def name2idx(self, name: int):
        return self.node_map[name]

    def idx2name(self, idx: int):
        return self.node_name[idx]

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
    def map_group(self, n:int, m: int, group: list[int]) -> (int, int):
        new_group = [0] * n
        g_cnt = 0
        old_new_map = dict[int, int]()
        for i, g in enumerate(group):
            if g == -1:
                new_group[i] = g_cnt
                g_cnt += 1
            else:
                if g in old_new_map:
                    new_group[i] = old_new_map[g]
                else:
                    new_group[i] = g_cnt
                    old_new_map[g] = g_cnt
                    g_cnt += 1
        return g_cnt, new_group


    def sortItems(self, n: int, m: int, group: List[int]
                  , beforeItems: List[List[int]]) -> List[int]:
        m, group = self.map_group(n, m, group)

        group_nodes_list = [list[int]() for _ in range(m)]
        group_inside_order_list = [list[int]() for _ in range(m)]
        group_node_set_list = [set[int]() for _ in range(m)]
        for i, g in enumerate(group):
            # if g == -1:
            #     continue
            group_nodes_list[g].append(i)
            group_node_set_list[g].add(i)

        group_node_before_list = [set[int]() for _ in range(m)]

        sub_graph_list = [Graph(len(group_nodes), group_nodes)
                          for group_nodes in group_nodes_list]
        for i, group_nodes in enumerate(group_nodes_list):
            sub_graph = sub_graph_list[i]
            for node in group_nodes:
                for before_node in beforeItems[node]:
                    if before_node in group_node_set_list[i]:
                        sub_graph.add_edge(
                            sub_graph.name2idx(before_node), sub_graph.name2idx(node))
                    else:
                        group_node_before_list[i].add(before_node)
            cd = CycleDetect(sub_graph)
            if cd.cycle_detected():
                return []
            ts = TopologicalSort(sub_graph)
            group_inside_order_list[i] = list(map(sub_graph.idx2name, ts.get_order()))
            # print(group_nodes_list)
            # print(group_inside_order_list[i])
            # print(group_node_before_list[i])

        group_node_before_list = [list(map(lambda x: group[x], before_list))
                                  for before_list in group_node_before_list]
        big_graph = Graph(m, list(range(m)))
        for g, node_before in enumerate(group_node_before_list):
            for node in node_before:
                big_graph.add_edge(node, g)
        cd = CycleDetect(big_graph)
        if cd.cycle_detected():
            return []
        ts = TopologicalSort(big_graph)
        ans = []
        for i in ts.get_order():
            ans.extend(group_inside_order_list[i])
        return ans


data = [
    8
    , 2
    , [-1, -1, 1, 0, 0, 1, 0, -1]
    , [[], [6], [5], [6], [3], [], [4], []]
]
r = Solution().sortItems(*data)
print(r)
