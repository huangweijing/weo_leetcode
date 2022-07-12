from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = list[TreeNode]()
        if root is None:
            return result
        result.append(root.val)
        q = deque()
        q.append(root)
        while len(q) > 0:
            layer_list = list[TreeNode]()
            while len(q) > 0:
                node = q.popleft()
                if node.left is not None:
                    layer_list.append(node.left)
                if node.right is not None:
                    layer_list.append(node.right)
            if len(layer_list) == 0:
                break
            q.extend(layer_list)
            result.append(layer_list[-1].val)
        return result


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

null = None
tree = make_leetree([])
r = Solution().rightSideView(tree)
print(r)