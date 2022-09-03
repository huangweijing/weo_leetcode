from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def exists(self, root: TreeNode, k: int) -> bool:
        if root is None:
            return False
        elif root.val == k:
            return True
        elif root.val < k:
            return self.exists(root.right, k)
        elif root.val > k:
            return self.exists(root.left, k)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        s = list[TreeNode]()
        s.append(root)
        while len(s) > 0:
            node = s.pop()
            if node.left is not None:
                s.append(node.left)
            if node.right is not None:
                s.append(node.right)
            if node.val == k - node.val:
                continue
            else:
                if self.exists(root, k - node.val):
                    return True
        return False


def make_leetree(data_list: list[int]) -> TreeNode:
    idx = 0
    root = TreeNode(data_list[idx])
    idx += 1
    node_queue = deque[TreeNode]()
    node_queue.append(root)
    while len(node_queue) > 0 and idx < len(data_list):
        node = node_queue.popleft()
        if data_list[idx] is not None:
            node.left = TreeNode(data_list[idx])
            node_queue.append(node.left)
        else:
            node.left = None
        idx += 1
        if idx == len(data_list):
            break
        if data_list[idx] is not None:
            node.right = TreeNode(data_list[idx])
            node_queue.append(node.right)
        else:
            node.right = None
        idx += 1
    return root

tree = make_leetree([2, 1, 3])
r = Solution().findTarget(tree, 4)
print(r)