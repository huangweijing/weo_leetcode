from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 1
        queue = deque([ (root, 0) ])
        while len(queue) > 0:
            new_queue = deque()
            while len(queue) > 0:
                node, idx = queue.popleft()
                if node.left is not None:
                    new_queue.append((node.left, idx * 2 + 1))
                if node.right is not None:
                    new_queue.append((node.right, idx * 2 + 2))
            if len(new_queue) > 0:
                # print(new_queue)
                ans = max(ans, new_queue[-1][1] - new_queue[0][1] + 1)
            queue = new_queue
        return ans



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

null = None
data = make_leetree([1,3,2,5,null,null,9,6,null,7])
r = Solution().widthOfBinaryTree(data)
print(r)