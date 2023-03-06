from typing import List, Optional
from functools import cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        # self.val_dict = dict[int, set[TreeNode]]()
        self.node_id_set = set[str]()
        self.ans_id_set = set[str]()
        self.ans = []

    def preorder(self, root: TreeNode) -> str:
        if root is None:
            return ""
        node_id = "(" + str(root.val)
        if root.left is not None:
            node_id += ",L:" + self.preorder(root.left)
        if root.right is not None:
            node_id += ",R:" + self.preorder(root.right)
        node_id += ")"
        if node_id in self.node_id_set:
            if node_id not in self.ans_id_set:
                self.ans_id_set.add(node_id)
                self.ans.append(root)
        else:
            self.node_id_set.add(node_id)
        return node_id

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.preorder(root)
        return self.ans

