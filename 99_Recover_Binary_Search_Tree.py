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
        self.parent_hash = dict[TreeNode, TreeNode]()
        self.sorted_list: list[int] = []
        self.node_list: list[TreeNode] = []

    def save_tree_to_list(self, root:Optional[TreeNode]):
        if root is None:
            return
        if root.left is not None:
            self.parent_hash[root.left] = root
        if root.right is not None:
            self.parent_hash[root.right] = root
        self.save_tree_to_list(root.left)
        self.sorted_list.append(root.val)
        self.node_list.append(root)
        self.save_tree_to_list(root.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.save_tree_to_list(root)

        recover_list: list[int] = []
        for idx in range(len(self.sorted_list) - 1):
            if self.sorted_list[idx] >= self.sorted_list[idx + 1]:
                recover_list.append(idx)
        if len(recover_list) == 1:
            idx = recover_list.pop()
            idx2 = idx + 1
            swap = self.node_list[idx].val
            self.node_list[idx].val = self.node_list[idx2].val
            self.node_list[idx2].val = swap
        elif len(recover_list) == 2:
            idx = recover_list[0]
            idx2 = recover_list[1] + 1
            swap = self.node_list[idx].val
            self.node_list[idx].val = self.node_list[idx2].val
            self.node_list[idx2].val = swap




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

def print_tree(root_node: TreeNode):
    print_list: list[int] = []
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

null = None
tree = make_leetree([1,3,null,null,2])
print_tree(tree)
sol = Solution()
sol.recoverTree(tree)
print_tree(tree)