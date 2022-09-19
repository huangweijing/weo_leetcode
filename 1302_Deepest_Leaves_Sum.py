from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        node_list = [ root ]
        sum_val = 0
        while len(node_list) > 0:
            new_node_list = []
            sum_val = 0
            while len(node_list) > 0:
                node = node_list.pop()
                sum_val += node.val
                if node.left is not None:
                    new_node_list.append(node.left)
                if node.right is not None:
                    new_node_list.append(node.right)
            node_list = new_node_list
        return sum_val