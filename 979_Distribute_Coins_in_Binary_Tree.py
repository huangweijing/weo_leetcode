from typing import Optional
from functools import cache
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.surplus_coin = dict[TreeNode, int]()

    @cache
    def get_surplus_coin(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root in self.surplus_coin:
            return self.surplus_coin[root]
        ans = root.val - 1
        ans += self.get_surplus_coin(root.left)
        ans += self.get_surplus_coin(root.right)
        self.surplus_coin[root] = ans
        return ans

    def my_sol(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ans = 0
        sp_left = self.get_surplus_coin(root.left)
        sp_right = self.get_surplus_coin(root.right)
        if sp_left > 0:
            ans += sp_left
            root.left.val = root.left.val - sp_left
            self.surplus_coin[root.left] = 0
        if sp_right > 0:
            ans += sp_right
            root.right.val = root.right.val - sp_right
            self.surplus_coin[root.right] = 0
        if sp_left < 0:
            ans += abs(sp_left)
            root.left.val -= abs(sp_left)
            self.surplus_coin[root.left] = 0
        if sp_right < 0:
            ans += abs(sp_right)
            root.right.val -= abs(sp_right)
            self.surplus_coin[root.right] = 0
        ans += self.my_sol(root.left)
        ans += self.my_sol(root.right)
        return ans

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.get_surplus_coin(root)
        return self.my_sol(root)

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

data = make_leetree([3,0,4,0,0,0,0,1,2,0,0,0,1,3,1])
r = Solution().distributeCoins(data)
print(r)