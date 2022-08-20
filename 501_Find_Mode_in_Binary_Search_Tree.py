# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.val_cnt = dict[int, int]()

    def traverse(self, root: TreeNode):
        if root is None:
            return
        else:
            if root.val not in self.val_cnt:
                self.val_cnt[root.val] = 0
            self.val_cnt[root.val] += 1

        if root.left is not None:
            self.traverse(root.left)
        if root.right is not None:
            self.traverse(root.right)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        result = list[int]()
        max_cnt = 0
        for key in self.val_cnt.keys():
            if self.val_cnt[key] > max_cnt:
                max_cnt = self.val_cnt[key]
                result = list[int]()
            if self.val_cnt[key] == max_cnt:
                result.append(key)
        result.sort()
        return result
