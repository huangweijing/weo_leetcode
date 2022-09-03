from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        tree_map = dict[int, TreeNode]()
        parent_map = dict[int, int]()
        for desc in descriptions:
            parent_map[desc[1]] = desc[0]
            tree_map[desc[0]] = TreeNode(desc[0])
            if desc[1] not in tree_map:
                tree_map[desc[1]] = TreeNode(desc[1])

        for desc in descriptions:
            node = tree_map[desc[0]]
            son = tree_map[desc[1]]
            if desc[2] == 1:
                node.left = son
            else:
                node.right = son

        root = descriptions[0][0]
        while True:
            if root not in parent_map:
                return tree_map[root]
            root = parent_map[root]


