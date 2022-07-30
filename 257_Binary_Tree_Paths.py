# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.sol = list[str]()

    def my_path(self, root, path: str):
        if root is None:
            return
        if len(path) == 0:
            path = f"{root.val}"
        else:
            path += f"->{root.val}"
        if root.left is None and root.right is None:
            self.sol.append(path)
        else:
            if root.left is not None:
                self.my_path(root.left, path)
            if root.right is not None:
                self.my_path(root.right, path)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.my_path(root, "")
        return self.sol



