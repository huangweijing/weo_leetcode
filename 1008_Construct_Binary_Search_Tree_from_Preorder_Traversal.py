from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(val=preorder[0])
        left_idx = 1
        left_tree_arr, right_tree_arr = [], []
        while left_idx < len(preorder):
            if preorder[left_idx] < root.val:
                left_tree_arr.append(preorder[left_idx])
            if preorder[left_idx] > root.val:
                right_tree_arr.append(preorder[left_idx])
            left_idx += 1
        left_tree = self.bstFromPreorder(left_tree_arr)
        right_tree = self.bstFromPreorder(right_tree_arr)
        root.left = left_tree
        root.right = right_tree
        return root


