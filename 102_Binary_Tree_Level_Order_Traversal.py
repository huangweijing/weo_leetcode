from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result
        q = deque()
        q.append(root)
        while len(q) > 0:
            layer = []
            while len(q) > 0:
                node = q.popleft()
                layer.append(node)
            for node in layer:
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            val_layer = [node.val for node in layer]
            result.append(val_layer)
        return result