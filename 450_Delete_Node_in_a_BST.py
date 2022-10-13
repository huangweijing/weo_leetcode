from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delete_min(self, root: TreeNode) -> TreeNode:
        cur = root
        node_parent = None
        while cur.left is not None:
            node_parent = cur
            cur = cur.left
        if node_parent is not None:
            node_parent.left = cur.right
        return cur

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val == key:
            if root.right is None:
                return root.left
            else:
                new_node = self.delete_min(root.right)
                new_node.left = root.left
                if new_node.right != root.right and new_node != root.right:
                    new_node.right = root.right
            return new_node
        return root

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
            print_list.append("null")
            continue
        print_list.append(node.val)
        node_queue.append(node.left)
        node_queue.append(node.right)
    print("[" + ",".join(map(str, print_list)) + "]")

null = None
data_tree = make_leetree([5,3,6,2,4,null,7])
data_key = 3
r = Solution().deleteNode(data_tree, data_key)
print_tree(r, [])

