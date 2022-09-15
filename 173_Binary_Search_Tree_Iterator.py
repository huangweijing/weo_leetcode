from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.current = -1
        self.order_list = []
        self.inorder(root)

    def inorder(self, node: TreeNode):
        if node is None:
            return
        if node.left is not None:
            self.inorder(node.left)
        self.order_list.append(node.val)
        if node.right is not None:
            self.inorder(node.right)

    def next(self) -> int:
        self.current += 1
        return self.order_list[self.current]

    def hasNext(self) -> bool:
        return self.current < len(self.order_list) - 1