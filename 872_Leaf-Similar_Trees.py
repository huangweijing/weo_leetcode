from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root: TreeNode, node_list: list[int]):
            if root is None:
                return
            dfs(root.left, node_list)
            if root.left is None and root.right is None:
                node_list.append(root.val)
            dfs(root.right, node_list)

        nl1, nl2 = [], []
        dfs(root1, nl1)
        dfs(root2, nl2)
        # print(nl1, nl2)
        return nl1 == nl2


