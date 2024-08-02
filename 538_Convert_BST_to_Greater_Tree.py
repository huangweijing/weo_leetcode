from typing import Optional
from functools import cache


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @cache
    def sum_greater(self, root: TreeNode, parent_sum_greater: int) -> TreeNode:
        if root is None:
            return None
        new_node = TreeNode(val=self.sum_node(root.right) + root.val + parent_sum_greater)
        new_node.right = self.sum_greater(root.right, parent_sum_greater)
        new_node.left = self.sum_greater(root.left, new_node.val)
        return new_node
        

    @cache
    def sum_node(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return root.val + self.sum_node(root.left) + self.sum_node(root.right)
    

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.sum_greater(root, 0)
        