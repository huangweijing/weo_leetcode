# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.parent = dict[TreeNode, TreeNode]()

    def common_root(self, stk: set[TreeNode]) -> TreeNode:
        if len(stk) == 1:
            return stk.pop()
        while len(stk) > 0:
            node_set = set[TreeNode]()
            while len(stk) > 0:
                node = stk.pop()
                node_set.add(self.parent[node])
            if len(node_set) == 1:
                return node_set.pop()
            stk = node_set
        return None

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        stk = set[TreeNode]([root])
        while len(stk) > 0:
            new_stk = set[TreeNode]()
            for node in stk:
                if node.left is not None:
                    self.parent[node.left] = node
                    new_stk.add(node.left)
                if node.right is not None:
                    self.parent[node.right] = node
                    new_stk.add(node.right)
            if len(new_stk) == 0:
                return self.common_root(stk)
            stk = new_stk
