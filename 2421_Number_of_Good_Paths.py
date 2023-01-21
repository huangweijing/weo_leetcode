from typing import List
from collections import defaultdict

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

class TreeNode:
    def __init__(self, node_id=-1, val=0, parent=None, children=[]):
        self.val = val
        self.children = children
        self.parent = parent
        self.node_id = node_id

class Solution:
    def __init__(self):
        self.g = Graph(0)
        self.vals = []
        self.max_path = dict[str, int]()
        self.node_list = list[TreeNode]()

    def build_tree(self, parent: int, current:int) -> TreeNode:
        root = TreeNode(current, self.vals[current], parent, [])
        adj_list = self.g.get_adjacent_vertex(current)
        for adj in adj_list:
            if adj == parent:
                continue
            child = self.build_tree(current, adj)
            root.children.append(child)
        self.node_list[current] = root
        return root

    def get_max_path_to_root(self, node: int):
        tree_node = self.node_list[node]
        max_val = 0
        while tree_node is not None:
            self.max_path[f"{node},{tree_node.node_id}"] = max(max_val, tree_node.val)
            tree_node = tree_node.parent

    def get_common_ancestor(self, node1: int, node2: int) -> TreeNode:
        tree_node1 = self.node_list[node1]
        tree_node2 = self.node_list[node2]
        ancestor_set = set()
        while tree_node1 is not None:
            ancestor_set.add(tree_node1)
            tree_node1 = tree_node1.parent
        while tree_node2 is not None:
            if tree_node2 in ancestor_set:
                return tree_node2
            tree_node2 = tree_node2.parent
        return None

    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        self.vals = vals
        self.g = Graph(len(vals))
        self.node_list = [None] * len(vals)
        for edge in edges:
            self.g.add_edge(edge[0], edge[1])
        root = self.build_tree(None, 0)

        val_dict = defaultdict(lambda : list[int]())
        for i, val in enumerate(vals):
            val_dict[val].append(i)
        for key, val in val_dict.items():
            if len(val) > 1:
                

d = dict[list[int], int]()
d[[1, 2]] = 3
