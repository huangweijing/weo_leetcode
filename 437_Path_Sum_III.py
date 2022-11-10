from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.prefix_sum_dict = dict[TreeNode, int]()
        self.parent_dict = dict[TreeNode, TreeNode]()

    def set_prefix_sum(self, root: TreeNode, parent: TreeNode):
        if root is None:
            return
        self.parent_dict[root] = parent
        if parent is None:
            parent_prefix_sum = 0
        else:
            parent_prefix_sum = self.prefix_sum_dict[parent]
        self.prefix_sum_dict[root] = root.val + parent_prefix_sum
        self.set_prefix_sum(root.left, root)
        self.set_prefix_sum(root.right, root)

    def get_path_sum(self, to_node: TreeNode, from_node: TreeNode):
        if to_node == from_node:
            return to_node.val
        if self.parent_dict[from_node] is None:
            return self.prefix_sum_dict[to_node]
        else:
            return self.prefix_sum_dict[to_node] - self.prefix_sum_dict[self.parent_dict[from_node]]

    def get_path_sum_children(self, root: TreeNode, target_sum: int) -> int:
        ans, stk = 0, [root]
        while len(stk) > 0:
            node = stk.pop()
            if self.get_path_sum(node, root) == target_sum:
                ans += 1
            if node.left is not None:
                stk.append(node.left)
            if node.right is not None:
                stk.append(node.right)
        return ans

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        self.set_prefix_sum(root, None)
        ans, stk = 0, [root]
        while len(stk) > 0:
            node = stk.pop()
            ans += self.get_path_sum_children(node, targetSum)
            if node.left is not None:
                stk.append(node.left)
            if node.right is not None:
                stk.append(node.right)
        return ans
