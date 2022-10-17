from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is not None:
            if root1.val == root2.val:
                if (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or \
                    (self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right)):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False