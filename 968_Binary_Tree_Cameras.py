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
        self.cache = dict[TreeNode, int]()

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if root in self.cache.keys():
            return self.cache[root]

        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        else:
            # camra in root
            camera1 = 1
            if root.left is not None:
                left_node_p1 = self.minCameraCover(root.left.left) + self.minCameraCover(root.left.right)
                left_node_p2 = self.minCameraCover(root.left)
                camera1 += min(left_node_p1, left_node_p2)
            if root.right is not None:
                right_node_p1 = self.minCameraCover(root.right.left) + self.minCameraCover(root.right.right)
                right_node_p2 = self.minCameraCover(root.right)
                camera1 += min(right_node_p1, right_node_p2)

            # camra in left
            camera2 = 9999999
            if root.left is not None:
                camera2 = 1
                if root.left.left is not None:
                    left_node_p1 = self.minCameraCover(root.left.left.left) + self.minCameraCover(root.left.left.right)
                    left_node_p2 = self.minCameraCover(root.left.left)
                    camera2 += min(left_node_p1, left_node_p2)
                if root.left.right is not None:
                    right_node_p1 = self.minCameraCover(root.left.right.left) + self.minCameraCover(root.left.right.right)
                    right_node_p2 = self.minCameraCover(root.left.right)
                    camera2 += min(right_node_p1, right_node_p2)
                camera2 += self.minCameraCover(root.right)

            # camra in right
            camera3 = 9999999
            if root.right is not None:
                camera3 = 1
                if root.right.left is not None:
                    left_node_p1 = self.minCameraCover(root.right.left.left) + self.minCameraCover(root.right.left.right)
                    left_node_p2 = self.minCameraCover(root.right.left)
                    camera3 += min(left_node_p1, left_node_p2)
                if root.right.right is not None:
                    right_node_p1 = self.minCameraCover(root.right.right.left) + self.minCameraCover(root.right.right.right)
                    right_node_p2 = self.minCameraCover(root.right.right)
                    camera3 += min(right_node_p1, right_node_p2)
                camera3 += self.minCameraCover(root.left)
            # print(f"camera: camera1={camera1}, camera2={camera2}, camera3={camera3}")

        result = min(camera1, camera2, camera3)
        self.cache[root] = result
        return result




def make_tree(data_list: list[int], root_idx:int=0) -> TreeNode:
    if root_idx >= len(data_list):
        return None
    if data_list[root_idx] is None:
        return None

    root_node: TreeNode = TreeNode()
    root_node.val = data_list[root_idx]

    root_node.left = make_tree(data_list, (root_idx << 1) + 1)
    root_node.right = make_tree(data_list, (root_idx << 1) + 2)

    return root_node


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
# tree = make_tree([0,0,None,0,None,0,None,None,0])
tree = make_leetree([0,0,0,0,0,0,0,0,0,0,null,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,null,0,0,0,null,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,null,null,0,0,0,0,0,0,0,0,null,null,0,null,0,0,0,0,0,0,0,0,0,0,0,0,null,null,0,null,0,0,null,0,null,0,0,0,0,0,null,null,null,null,0,0,0,0,null,null,0,0,0,0,0,0,null,null,null,null,0,null,null,0,null,null,null,null,0,0,0,0,0,null,0,0,null,null,0,0,0,0,0,null,0,null,0,0,0,0,0,0,null,null,0,0,0,0,0,null,null,0,0,null,0,null,0,null,0,0,0,null,0,0,null,0,0,null,0,0,0,0,0,0,0,0,0,0,null,0,0,0,null,0,0,0,0,0,null,0,0,0,null,null,0,0,0,0,0,0,null,0,0,null,null,0,null,0,0,null,0,0,null,0,0,0,0,0,null,0,null,0,null,null,null,0,0,0,0,0,0,null,null,null,0,0,0,0,0,null,null,null,0,null,null,0,null,null,null,null,0,null,0,null,0,0,0,null,null,0,null,null,null,0,0,0,null,null,0,0,0,0,null,null,0,0,null,0,0,0,null,0,0,null,0,null,0,0,0,0,null,0,0,0,0,0,0,0,null,0,null,null,null,0,0,0,0,0,null,0,0,0,0,0,0,0,0,0,null,null,null,null,0,null,null,null,null,0,0,null,null,0,null,0,0,0,0,0,null,0,0,0,0,null,0,null,null,null,null,null,null,null,0,0,0,0,null,0,0,null,0,0,0,0,0,0,0,null,0,null,null,0,null,null,null,null,null,null,0,0,null,null,0,null,null,null,null,null,0,null,0,0,0,null,0,0,0,0,0,0,0,0,null,0,0,0,0,0,null,null,null,0,0,null,0,0,null,0,null,null,0,0,null,null,null,0,0,null,null,null,null,0,0,0,0,0,null,0,0,null,0,0,0,null,0,0,0,0,null,0,null,0,0,0,0,0,null,null,null,0,0,0,0,0,0,0,null,null,null,null,0,null,0,null,null,null,0,0,0,null,0,null,null,null,0,null,0,0,null,null,null,0,null,null,0,null,null,0,0,0,null,0,null,null,null,null,0,0,0,0,0,0,0,0,0,0,null,0,0,0,0,null,0,null,null,0,null,null,0,0,null,null,0,0,null,0,0,0,0,0,0,0,0,0,0,0,null,0,0,0,0,0,0,0,0,null,0,0,0,0,0,0,0,null,null,0,null,null,0,null,0,null,0,null,0,0,0,0,0,null,null,null,null,null,null,0,0,null,0,0,null,0,0,0,0,null,null,null,null,null,0,null,null,0,null,0,null,null,null,0,null,null,null,null,0,0,0,0,null,null,0,null,null,null,0,0,0,null,0,0,0,0,0,0,null,0,null,null,0,0,null,null,null,null,0,null,null,null,null,null,null,null,null,0,null,null,null,null,0,null,0,null,0,null,0,0,null,0,null,null,0,null,0,null,0,null,null,0,0,null,0,null,0,0,0,0,0,0,null,0,0,0,0,null,null,null,null,null,0,0,0,0,0,0,null,0,0,0,null,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,null,0,0,0,0,0,null,0,null,0,0,0,0,0,0,null,0,0,0,null,null,null,null,null,null,null,null,0,null,0,null,0,null,null,null,0,null,null,null,0,0,null,null,null,0,0,0,0,0,0,null,null,null,null,null,0,0,null,0,0,null,null,null,null,null,null,0,null,0,null,null,null,0,0,0,null,0,0,null,0,0,null,null,null,null,null,null,0,0,0,0,0,null,null,0,null,null,0,0,0,0,0,0,0,null,null,null,0,0,null,null,null,null,null,null,null,null,null,null,0,null,null,null,null,0,null,null,null,null,null,null,null,0,null,null,0,null,0,0,null,null,0,null,null,null,0,null,null,null,null,null,null,null,null,null,null,null,null,0,null,null,null,null,0,0,null,0,0,0,null,null,null,null,0,0,null,null,null,null,0,0,0,0,null,null,0,0,null,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,null,null,null,null,null,0,0,null,null,null,null,null,null,null,null,null,null,null,null,null,0,0,0,0,null,null,0,null,null,null,null,null,0,null,null,null,null,null,null,0,0,null,0,null,0,0,0,0,null,null,null,null,null,null,0,0,0,0,0,0,0,0,0,null,null,null,null,0,0,null,null,null,null,0,0,null,null,0,null,0,null,0,null,null,0,null,null,null,null,0,null,0,null,null,null,null,0,0,null,0,0,0,null,0,0,0,null,0,null,null,null,null,0,null,null,null,null,null,null,null,null,0,0,0,0,null,0,null,0,null,0,null,0,0,0,0,0,null,0,0,0,null,null,null,null,0,0,0,0,null,0,0,null,null,0,null,null,0,null,0,0,null,0,0,0,null,0,0,null,null,null,0,0,null,null,null,null,null,0,0,0,null,0,0,0,0,0,0,0,0,null,null,0,0,null,0,null,null,null,0,0,null,null,null,0,0,null,0,null,null,0,null,null,0,0,null,null,null,0,0,null,null,0,null,0,null,0,0,null,null,null,0,0,null,null,null,null,0,0,null,0,null,null,null,null,0,0,0,0,0,0,null,null,null,0,0,null,0,null,null,null,null,0,null,0,null,null,0,0,null,null,0,0,0,0,null,0,null,null,null,null,null,null,null,null,null,0,0,0,null,0,null,null,0,0,null,0,0,0,null,0,null,null,null,0,null,0,null,null,0,null,0,0,0,0,0,0,0,0,0,null,null,0,0,0,null,null,null,null,null,0,0,null,null,null,null,0,0,0,0,0,null,0,0,0,null,null,null,null,null,0,null,null,0,0,0,0,0,null,null,0,0,0,0,null,null,null,0,0,null,null,0,null,null,0,0,0,null,0,null,0,null,0,null,null,0,0,null,null,null,null,null,null,null,null,null,null,null,null,0,null,null,0,0,null,null,null,null,null,0,null,0,0,0,0,null,0,0,0,null,null,0,null,null,0,null,null,0,null,null,null,null,null,null,0,0,0,0,0,0,0,null,null,null,null,null,null,0,0,null,0,null,0,null,null,null,null,null,0,null,null,null,null,null,0,0,0,0,null,null,null,null,null,null,null,null,0,0,0,0,0,null,0,0,null,0,0,0,0,0,0,0,null,0,0,0,null,null,0,null,null,null,null,null,null,null,null,0,null,null,null,0,null,0,null,0,0,null,null,0,0,null,0,0,0,null,0,0,0,null,0,null,null,null,null,0,null,0,null,0,null,null,null,null,null,null,0,0,0,null,null,0,null,null,null,0,0,null,null,null,null,0,null,0,null,null,null,0,null,0,0,0,0,0,0,null,0,0,null,null,null,0,null,0,null,null,0,null,null,null,null,null,null,null,null,null,null,0,null,0,0,null,null,null,null,0,null,0,null,null,null,null,0,0,null,null,0,null,null,0,0,0,0,null,0,null,null,0,null,null,null,0,null,0,0,0,null,0,0,0,0,0,null,null,null,null,null,0,null,0,null,0,null,null,0,null,null,null,null,null,null,null,null,null,0,null,0,0,0,null,null,null,null,0,null,null,null,0,null,null,null,null,0,null,null,null,null,null,null,null,null,0,null,0,null,null,null,0,null,null,null,null,null,0,null,0,0,0,0,null,null,null,0,0,0,null,0,0,0,null,0,null,null,null,null,null,null,null,null,null,null,null,null,0,0,0,null,null,null,null,null,null,null,0,0,0,0,0,0,null,null,null,0,0,null,null,null,0,0,null,0,0,0,0,null,null,null,0,null,null,null,null,null,null,null,null,null,0,null,null,null,null,null,null,null,0,0,0,0,0,null,0,0,null,null,null,0,0,0,0,0,null,null,null,null,null,0,0,0,null,0,null,null,null,null,0,0,0,null,null,null,0,null,null,0,0,null,null,0,0,null,null,null,null,null,null,null,0,null,0,null,null,null,null,0,0,null,null,0,0,0,0,0,null,null,0,null,null,0,0,0,0,0,0,null,null,null,0,null,null,null,0,0,null,null,null,null,null,null,null,null,null,null,0,0,null,0,null,null,0,null,0,null,null,null,null,null,null,null,0,null,null,null,null,null,null,null,0,null,0,null,null,0,null,null,0,0,null,null,null,0,null,null,0,0,null,null,0,0,0,0,0,0,0,0,null,null,0,0,null,null,null,null,null,null,null,null,0,0,0,null,null,null,null,0,null,0,null,0,null,null,null,null,0,0,null,null,null,null,null,0,0,0,null,0,null,null,null,0,null,null,0,0,null,null,null,null,0,null,null,null,null,null,0,0,null,null,null,null,null,null,0,0,null,null,null,0,null,null,null,null,null,null,null,null,null,null,0,null,null,null,null,null,0,0,null,null,null,null,null,null,0,0,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0])
# tree = make_leetree([0,null,0,0,0,null,null,0,0])
tree_data = []
print_tree(tree, tree_data)
sol = Solution()
r = sol.minCameraCover(tree)
print(r)