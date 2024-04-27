from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.parent = dict[TreeNode: TreeNode]()

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        q = [root]
        leaf_list = []
        while len(q) > 0:
            new_q = []
            while len(q) > 0:
                node = q.pop()
                if node.left is None and node.right is None:
                    leaf_list.append(node)
                if node.left is not None:
                    self.parent[node.left] = node
                    new_q.append(node.left)
                if node.right is not None:
                    self.parent[node.right] = node
                    new_q.append(node.right)
            q = new_q

        ans = ""
        q = leaf_list
        while len(q) > 0:
            min_val = 26
            new_q = []
            could_return = False
            for node in q:
                if node.val == min_val:
                    if node not in self.parent:
                        could_return = True
                    else:
                        new_q.append(self.parent[node])
                elif node.val < min_val:
                    could_return = False
                    if node not in self.parent:
                        could_return = True
                    else:
                        new_q = [self.parent[node]]
                    min_val = node.val
            ans += chr(ord("a") + min_val)
            if could_return:
                return ans
            q = new_q
        return ans




