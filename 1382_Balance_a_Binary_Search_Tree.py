# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def arr2tree(self, arr: list[int], left_idx: int, right_idx: int) -> TreeNode:
        if left_idx > right_idx:
            return None
        if left_idx == right_idx:
            return TreeNode(arr[left_idx])
        mid_idx = left_idx + (right_idx - left_idx) // 2
        left_tree = self.arr2tree(arr, left_idx, mid_idx - 1)
        right_tree = self.arr2tree(arr, mid_idx + 1, right_idx)
        return TreeNode(arr[mid_idx], left_tree, right_tree)

    def tree2arr(self, root: TreeNode) -> list[int]:
        left, right = [], []
        if root.left is not None:
            left = self.tree2arr(root.left)
        if root.right is not None:
            right = self.tree2arr(root.right)
        left.append(root.val)
        left.extend(right)
        return left


    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = self.tree2arr(root)
        return self.arr2tree(arr, 0, len(arr) - 1)
