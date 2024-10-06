from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.tree_node = dict[int, TreeNode]()
        self.parent = dict[int, int]()

    def record_node(self, root: TreeNode):
        if root is None:
            return
        self.tree_node[root.val] = root
        if root.left is not None:
            self.parent[root.left.val] = root.val
            self.record_node(root.left)
        if root.right is not None:
            self.parent[root.right.val] = root.val
            self.record_node(root.right)

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.record_node(root)
        q = [[startValue, ""]]
        visited = set[int]()
        visited.add(startValue)
        while len(q) > 0:
            node = q.pop()
            val, path = node[0], node[1]
            if val == destValue:
                return path
            if val in self.parent and self.parent[val] not in visited:
                q.append([self.parent[val], path + "U"])
                visited.add(self.parent[val])
            if self.tree_node[val].left is not None and self.tree_node[val].left.val not in visited:
                q.append([self.tree_node[val].left.val, path + "L"])
                visited.add(self.tree_node[val].left.val)
            if self.tree_node[val].right is not None and self.tree_node[val].right.val not in visited:
                q.append([self.tree_node[val].right.val, path + "R"])
                visited.add(self.tree_node[val].right.val)
        return ""

