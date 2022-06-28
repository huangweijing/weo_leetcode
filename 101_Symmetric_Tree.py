# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_mirror(self, root1, root2) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        print(root1.val, root2.val)
        if root1.val == root2.val:
            return self.is_mirror(root1.left, root2.right) \
                   and self.is_mirror(root1.right, root2.left)
        else:
            return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_mirror(root.left, root.right)
