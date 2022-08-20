from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return None

        q = deque()
        q.append(root)
        result = list[int]()
        while len(q) > 0:
            result.append(q.copy())
            new_q = deque()
            num_list = list[int]()
            while len(q) > 0:
                node = q.popleft()
                num_list.append(node.val)
                if node.left is not None:
                    new_q.append(node.left)
                if node.right is not None:
                    new_q.append(node.right)
            q = new_q

        return result[-1][0].val

