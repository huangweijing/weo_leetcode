# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        if left_depth is 0:
            return right_depth + 1
        if right_depth is 0:
            return left_depth + 1

        return min(left_depth, right_depth) + 1
