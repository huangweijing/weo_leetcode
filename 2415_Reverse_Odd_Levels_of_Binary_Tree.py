from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 0
        node_list = deque([root])
        while len(node_list) > 0:
            new_node_list = deque()
            tmp_node_list = []
            node_val_list = []
            while len(node_list) > 0:
                node = node_list.popleft()
                if node.left is not None:
                    new_node_list.append(node.left)
                if node.right is not None:
                    new_node_list.append(node.right)
                tmp_node_list.append(node)
                node_val_list.append(node.val)
            if level & 1 == 1:
                for node in tmp_node_list:
                    node.val = node_val_list.pop()
            node_list = new_node_list
            level += 1
        return root
