class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.sum_val = 0

class Solution:
    def __init__(self):
        self.sum = 0

    def postorder(self, root: TreeNode):
        if root is None:
            return
        self.postorder(root.right)
        self.sum += root.val
        root.val = self.sum
        self.postorder(root.left)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.postorder(root)
        return root
