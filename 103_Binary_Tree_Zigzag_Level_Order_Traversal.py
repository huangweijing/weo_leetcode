# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque()
        result = []
        q.append(root)
        while len(q) > 0:
            layer = []
            node_layer = []
            while len(q) > 0:
                node = q.popleft()
                layer.append(node.val)
                node_layer.append(node)
            if len(result) & 1 == 1:
                layer.reverse()
            result.append(layer)

            for node in node_layer:
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

        return result

