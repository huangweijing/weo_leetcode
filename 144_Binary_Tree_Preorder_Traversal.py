# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        result.append(root.val)
        if root.left is not None:
            result.extend(self.preorderTraversal(root.left))
        if root.right is not None:
            result.extend(self.preorderTraversal(root.right))
        return result