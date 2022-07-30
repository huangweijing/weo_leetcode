from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.sol = list[list[int]]()

    def my_path_sum(self, root: Optional[TreeNode], targetSum: int
                    , route: list[int]):
        # print(root.val, targetSum)
        if root is None:
            return
        route.append(root.val)
        if root.val == targetSum and root.left is None and root.right is None:
            self.sol.append(route.copy())
        else:
            if root.left is not None:
                self.my_path_sum(root.left, targetSum - root.val, route)
            if root.right is not None:
                self.my_path_sum(root.right, targetSum - root.val, route)
        route.pop()


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.my_path_sum(root, targetSum, list[int]())
        return self.sol
