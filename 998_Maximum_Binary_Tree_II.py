from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val=val)
        if val > root.val:
            new_node = TreeNode(val=val)
            new_node.left = root
            return new_node
        else:
            root.right = self.insertIntoMaxTree(root=root.right, val=val)
            return root
        