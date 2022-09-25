# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.result = None

    def dfs(self, original: TreeNode, cloned: TreeNode, target: TreeNode):
        if self.result is not None:
            return
        if original is None:
            return
        if original == target:
            self.result = cloned
            return
        self.dfs(original.left, cloned.left, target)
        self.dfs(original.right, cloned.right, target)

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.dfs(original, cloned, target)
        return self.result

