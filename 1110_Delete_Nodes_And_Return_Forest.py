from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = list[TreeNode]()

    def my_del(self, root: TreeNode, to_del: set[int]) -> Optional[TreeNode]:
        if root is None:
            return None
        left, right = root.left, root.right
        deleted = False
        if root.val in to_del:
            deleted = True
            to_del.remove(root.val)

        root.left = self.my_del(left, to_del)
        root.right = self.my_del(right, to_del)
        if deleted:
            if root.left is not None:
                self.ans.append(root.left)
            if root.right is not None:
                self.ans.append(root.right)
            return None
        return root

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_del = set(to_delete)
        if root.val not in to_del:
            self.ans.append(root)
        self.my_del(root, to_del)
        return self.ans

