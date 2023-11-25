# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left_length = self.maxDepth(root.left)
        right_length = self.maxDepth(root.right)
        if abs(left_length - right_length) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

