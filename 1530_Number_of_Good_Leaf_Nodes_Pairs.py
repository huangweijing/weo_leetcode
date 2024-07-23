# from typing import 


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:

    def __init__(self) -> None:
        self.ans = 0
        # self.parent_dict = dict[int, TreeNode]()
        self.node_height = dict[TreeNode, int]()

    def calc_tree(self, root: TreeNode, height: int):
        if not root:
            return 0
        self.node_height[root] = height
        if root.left:
            # self.parent_dict[root.left] = root
            self.calc_tree(root.left, height + 1)
        if root.right:
            # self.parent_dict[root.right] = root
            self.calc_tree(root.right, height + 1)
    
    def my_sol(self, node: TreeNode) -> list[int]:
        ret, s1, s2 = [], [], []
        if not node.left and not node.right:
            ret = [node]
            return ret
        if node.left:
            s1 = self.my_sol(node.left)
            ret.extend(s1)
        if node.right:
            s2 = self.my_sol(node.right)
            ret.extend(s2)
        path0 = self.node_height[node]
        for n1 in s1:
            path1 = self.node_height[n1]
            for n2 in s2:
                path2 = self.node_height[n2]
                if path1 + path2 - path0 * 2 <= self.distance:
                    self.ans += 1
        return ret

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.distance = distance
        self.calc_tree(root, 0)
        self.my_sol(root)
        return self.ans
        