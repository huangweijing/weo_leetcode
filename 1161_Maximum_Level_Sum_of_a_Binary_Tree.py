# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        layer = 0
        node_list = [ root ]
        max_sum, max_layer = -math.inf, 0
        while len(node_list) > 0:
            layer += 1
            new_node_list = []
            sum_nodes = 0
            while len(node_list) > 0:
                node = node_list.pop()
                sum_nodes += node.val
                if node.left is not None:
                    new_node_list.append(node.left)
                if node.right is not None:
                    new_node_list.append(node.right)
            if sum_nodes > max_sum:
                max_sum = sum_nodes
                max_layer = layer
            node_list = new_node_list
        return max_layer