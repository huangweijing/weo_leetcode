class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        max_depth = 0
        for node in root.children:
            max_depth = max(self.maxDepth(node), max_depth)
        return max_depth + 1

