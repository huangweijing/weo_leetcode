from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        node_seq = [ root ]
        parent_dict = dict[TreeNode, TreeNode]()
        parent_val_dict = defaultdict(lambda : 0)
        while len(node_seq) > 0:
            new_node_seq = []
            layer_sum = 0
            for node in node_seq:
                layer_sum += node.val
            for node in node_seq:

                if node in parent_dict:
                    # print(f"node.val={node.val}, layer_sum={layer_sum}, parent_val_dict[node]={parent_val_dict[node]}")
                    node.val = layer_sum - parent_val_dict[parent_dict[node]]
                else:
                    # print(f"node.val={node.val}, layer_sum={layer_sum}")
                    node.val = 0

            while len(node_seq) > 0:
                node = node_seq.pop()
                if node.left is not None:
                    new_node_seq.append(node.left)
                    parent_dict[node.left] = node
                    parent_val_dict[node] += node.left.val
                if node.right is not None:
                    new_node_seq.append(node.right)
                    parent_dict[node.right] = node
                    parent_val_dict[node] += node.right.val
            # print(parent_val_dict)
            node_seq = new_node_seq
        return root