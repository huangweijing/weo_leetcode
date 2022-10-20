from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.val_set = set[int]()
        self.recover(root, 0)
        self.root = root


    def recover(self, root: TreeNode, val: int):
        if root is None:
            return
        root.val = val
        self.val_set.add(val)
        if root.left is not None:
            self.recover(root.left, val * 2 + 1)
        if root.right is not None:
            self.recover(root.right, val * 2 + 2)

    def find(self, target: int) -> bool:
        return target in self.val_set
