# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dp = dict[TreeNode, int]()

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root in self.dp.keys():
            return self.dp[root]

        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left_depth = 0
        if root.left is not None:
            left_depth = self.maxDepth(root.left)

        right_depth = 0
        if root.right is not None:
            right_depth = self.maxDepth(root.right)
        result = max(left_depth, right_depth) + 1
        self.dp[root] = result
        return result

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left_length = self.maxDepth(root.left)
        right_length = self.maxDepth(root.right)
        if -1 <= left_length - right_length <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

