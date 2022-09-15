"""
# Definition for a Node.
"""
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        q = deque()
        q.append(root)
        result = list[list[int]]()
        while len(q) > 0:
            new_q = deque()
            val_list = list[int]()
            while len(q) > 0:
                node = q.popleft()
                val_list.append(node.val)
                for child in node.children:
                    new_q.append(child)
            result.append(val_list)
            q = new_q
        return result

