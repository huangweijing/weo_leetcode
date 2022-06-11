from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = list[int]()
        left_result = self.inorderTraversal(root.left)
        right_result = self.inorderTraversal(root.right)
        result.extend(left_result)
        result.append(root.val)
        result.extend(right_result)
        return result