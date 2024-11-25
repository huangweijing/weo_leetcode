from typing import Optional
from functools import cache


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        # root = TreeNode()
        self.tree_size = []

    @cache
    def height(self, node: TreeNode) -> int:
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return max(self.height(node.left), self.height(node.right)) + 1
    
    @cache
    def is_perfect(self, node: TreeNode) -> bool:
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if self.height(node.left) == self.height(node.right) \
            and self.is_perfect(node.left) and self.is_perfect(node.right):
            return True
        return False

    @cache
    def size(self, node:TreeNode) -> int:
        if node is None:
            return 0
        if node.left is None and node.right is None:
            self.tree_size.append(1)
            return 1
        sum_size = self.size(node.left) + self.size(node.right) + 1
        if self.is_perfect(node):
            self.tree_size.append(sum_size)
        return sum_size

    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        self.size(root)
        if k > len(self.tree_size):
            return -1
        self.tree_size.sort(reverse=True)
        return self.tree_size[k - 1]