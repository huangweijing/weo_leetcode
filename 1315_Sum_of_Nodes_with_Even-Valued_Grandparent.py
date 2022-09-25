# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sum_grandparent(self, grand_node: TreeNode, parent_node: TreeNode):
        result = 0
        if parent_node.left is not None:
            if grand_node is not None and grand_node.val & 1 == 0:
                result += parent_node.left.val
            result += self.sum_grandparent(parent_node, parent_node.left)
        if parent_node.right is not None:
            if grand_node is not None and grand_node.val & 1 == 0:
                result += parent_node.right.val
            result += self.sum_grandparent(parent_node, parent_node.right)
        return result

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.sum_grandparent(None, root)

