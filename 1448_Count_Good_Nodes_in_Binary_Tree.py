from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def my_good_nodes(self, root:TreeNode, max_val: int) -> int:
        if root is None:
            return 0
        result = 0
        if root.val >= max_val:
            result += 1
        result += self.my_good_nodes(root.left, max(max_val, root.val))
        result += self.my_good_nodes(root.right, max(max_val, root.val))
        return result

    def goodNodes(self, root: TreeNode) -> int:
        return self.my_good_nodes(root, - 10 ** 4 - 1)
