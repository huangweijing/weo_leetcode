from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorder_flatten(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        cur = root
        root_left = root.left
        root_right = root.right
        if root_left is not None:
            ll = self.preorder_flatten(root_left)
            cur.left = None
            cur.right = ll
            while cur.right is not None:
                cur = cur.right
        if root_right is not None:
            ll = self.preorder_flatten(root_right)
            cur.left = None
            cur.right = ll
        return root

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.preorder_flatten(root)

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

def print_tree(root_node: TreeNode, print_list: list[int]):
    node_queue: deque[TreeNode] = deque[TreeNode]()
    node_queue.append(root_node)
    while len(node_queue) != 0:
        node = node_queue.popleft()
        if node is None:
            print_list.append(None)
            continue
        print_list.append(node.val)
        node_queue.append(node.left)
        node_queue.append(node.right)
    print(print_list)

def print_ll_tree(root_node: TreeNode):
    cur = root_node
    while cur is not None:
        print(f"{cur.val} ->", end="")
        cur = cur.right

null = None
tree = make_leetree([1,2,5,3,4,null,6])
Solution().preorder_flatten(tree)
print_ll_tree(tree)