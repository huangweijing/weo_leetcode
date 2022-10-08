from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.root = TreeNode()
        self.height = 0

    def exists(self, cmd: int) -> bool:
        if cmd >= (1 << self.height - 1):
            return False

        node = self.root
        level = 0
        while level < self.height - 1:
            bit_pos = self.height - 1 - level
            # print(f"bit_pos = {bit_pos}, cmd={cmd}, cmd >> (bit_pos - 1)={cmd >> (bit_pos - 1)}")
            # print(node.val)
            if cmd >> (bit_pos - 1) == 1:
                node = node.right
            else:
                node = node.left
            level += 1
            cmd = cmd & ((1 << bit_pos - 1) - 1)
        if node is None:
            return False
        else:
            return True

    def get_tree_height(self):
        self.height = 0
        cur = self.root
        while cur is not None:
            self.height += 1
            cur = cur.left
        return self.height

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.root = root
        self.get_tree_height()
        # print(self.height)
        l, r = 0, 1 << self.height - 1
        mid = (l + r) >> 1
        while l < r:
            mid_exists = self.exists(mid)
            mid1_exists = self.exists(mid + 1)
            # print(f"mid={mid}, mid_exists={mid_exists}, mid+1_exists={mid1_exists}")
            if mid_exists and not mid1_exists:
                return mid + (1 << (self.height - 1))
            if mid_exists:
                l = mid
            else:
                r = mid
            mid = (l + r) >> 1
        return None

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

data_tree = make_leetree([0])
sol = Solution()
result = sol.countNodes(data_tree)
print(result)
# print("----------")
# print(sol.exists(0b010))