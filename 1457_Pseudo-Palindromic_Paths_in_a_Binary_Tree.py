from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.result = 0

    def my_path(self, root: TreeNode, path: dict[int, int]):
        if root is None:
            return
        path[root.val] = path.get(root.val, 0) + 1
        if root.left is None and root.right is None:
            single = 0
            is_result = True
            for value in path.values():
                if value & 1 == 1:
                    if single >= 1:
                        is_result = False
                        break
                    else:
                        single = 1
            if is_result:
                self.result += 1
        if root.left is not None:
            self.my_path(root.left, path)
        if root.right is not None:
            self.my_path(root.right, path)
        path[root.val] -= 1

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.my_path(root, dict[int, int]())
        return self.result

