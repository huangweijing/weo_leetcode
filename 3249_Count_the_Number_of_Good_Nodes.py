from typing import List
from functools import cache
from collections import defaultdict

class TreeNode:
    def __init__(self, val: int):
        self.val = 0
        self.children = []

class Solution:
    def __init__(self):
        self.adj = defaultdict(lambda: set[int]())
        self.ans = 0

    def build_tree(self, cur: int, par: int) -> TreeNode:
        root = TreeNode(cur)
        for node in self.adj[cur]:
            if node != par:
                child = self.build_tree(node, cur)
                root.children.append(child)
        return root

    @cache
    def get_size(self, root: TreeNode) -> int:
        size = 0
        if root is not None:
            size += 1
            for child in root.children:
                size += self.get_size(child)
        return size

    def calc_good_nodes(self, root: TreeNode):
        sizes = set[int]()
        if root is not None:
            for child in root.children:
                sizes.add(self.get_size(child))
                self.calc_good_nodes(child)
        if len(sizes) <= 1:
            self.ans += 1
            # print(root.val)

    def countGoodNodes(self, edges: List[List[int]]) -> int:
        for edge in edges:
            self.adj[edge[0]].add(edge[1])
            self.adj[edge[1]].add(edge[0])
        root = self.build_tree(0, -1)
        self.calc_good_nodes(root)
        return self.ans


