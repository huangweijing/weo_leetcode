from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        node_list = [root]
        level = 1
        level_sum_arr = []
        while len(node_list) > 0:
            level_sum = 0
            new_node_list = []
            while len(node_list) > 0:
                node = node_list.pop()
                level_sum += node.val
                if node.left is not None:
                    new_node_list.append(node.left)
                if node.right is not None:
                    new_node_list.append(node.right)
            level_sum_arr.append(level_sum)
            node_list = new_node_list
            level += 1
        level_sum_arr.sort(reverse=True)
        if k > len(level_sum_arr):
            return -1
        return level_sum_arr[k - 1]
