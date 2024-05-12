from typing import Optional, List
import bisect


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def inorder(self, r: TreeNode) -> list[int]:
        ret = []
        if r is not None:
            ret.extend(self.inorder(r.left))
            ret.append(r.val)
            ret.extend(self.inorder(r.right))
        return ret

    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        arr = self.inorder(root)
        ans = []
        for query in queries:
            idx1 = bisect.bisect_right(arr, query) - 1
            if arr[idx1] == query:
                idx2 = idx1
            elif idx1 < len(arr) - 1:
                idx2 = idx1 + 1
            else:
                idx2 = -1
            ans.append([-1 if idx1 == -1 else arr[idx1]
                           , -1 if idx2 == -1 else arr[idx2]])
        return ans


