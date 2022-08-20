from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        q = deque()
        q.append(root)
        result = list[int]()
        while len(q) > 0:
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
            result.append(max(num_list))

        return result

