from typing import List
from collections import deque

class Graph:
    def __init__(self, vertex_count: int):
        self.vertex_adj_list = [set[int]() for x in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int):
        self.vertex_adj_list[v1].add(v2)
        self.vertex_adj_list[v2].add(v1)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_vertex(self, v) -> set[int]:
        return self.vertex_adj_list[v]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convert_graph(self, root: TreeNode) -> Graph:
        g = Graph(501)
        node_list = deque([root])
        while len(node_list) > 0:
            while len(node_list) > 0:
                node = node_list.pop()
                if node.left is not None:
                    g.add_edge(node.val, node.left.val)
                    node_list.appendleft(node.left)
                if node.right is not None:
                    g.add_edge(node.val, node.right.val)
                    node_list.appendleft(node.right)
        return g

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        g = self.convert_graph(root)
        node_arr = [target.val]
        visited = set[int]([target.val])
        while k > 0:
            k -= 1
            new_node_arr = list[int]()
            while len(node_arr) > 0:
                node = node_arr.pop()
                adj_node_list = g.get_adjacent_vertex(node)
                for adj_node in adj_node_list:
                    if adj_node not in visited:
                        new_node_arr.append(adj_node)
                        visited.add(adj_node)
            node_arr = new_node_arr
        return node_arr





