from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    # def my_insert(self, val: int, cur: TreeNode) -> TreeNode:
    #     if cur is None:
    #         return TreeNode(val, None, None)
    #     else:
    #         if val < cur.


    def insert(self, val: int) -> int:
        if self.root is None:
            self.root = TreeNode(val, None, None)
        else:
            if val < self.root.val:


    def get_root(self) -> Optional[TreeNode]:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()