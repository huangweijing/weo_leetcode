from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def get_left_branch(self, root: TreeNode) -> list[int]:
        ret = []
        cur = root
        while cur is not None:
            ret.append(cur)
            cur = cur.left
        return ret

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        stk1, stk2 = self.get_left_branch(root1), self.get_left_branch(root2)
        while len(stk1) > 0 or len(stk2) > 0:
            n1, n2 = None, None
            if len(stk1) > 0:
                n1 = stk1[-1]
            if len(stk2) > 0:
                n2 = stk2[-1]
            if n1 is not None and n2 is not None:
                if n1.val <= n2.val:
                    res.append(n1.val)
                    stk1.pop()
                    if n1.right is not None:
                        stk1.extend(self.get_left_branch(n1.right))
                else:
                    res.append(n2.val)
                    stk2.pop()
                    if n2.right is not None:
                        stk2.extend(self.get_left_branch(n2.right))
            elif n1 is None:
                res.append(n2.val)
                stk2.pop()
                if n2.right is not None:
                    stk2.extend(self.get_left_branch(n2.right))
            elif n2 is None:
                res.append(n1.val)
                stk1.pop()
                if n1.right is not None:
                    stk1.extend(self.get_left_branch(n1.right))
        return res



