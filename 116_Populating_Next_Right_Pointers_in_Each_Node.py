from typing import Optional
from collections import deque

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        que = deque()
        que.append(root)
        while len(que) > 0:
            node_list = list[Node]()
            while len(que) > 0:
                node = que.popleft()
                if node.left is not None:
                    node_list.append(node.left)
                if node.right is not None:
                    node_list.append(node.right)
            for i in range(len(node_list) - 1):
                node_list[i].next = node_list[i + 1]
            que.extend(node_list)
        return root
