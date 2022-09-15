from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n & 1 == 0:
            return None
        if n == 1:
            return [TreeNode()]
        result = []
        for i in range(1, n, 2):
            left_trees = self.allPossibleFBT(i)
            right_trees = self.allPossibleFBT(n - 1 - i)
            if left_trees is None or right_trees is None:
                continue
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode()
                    root.left = left
                    root.right = right
                    result.append(root)
        return result


