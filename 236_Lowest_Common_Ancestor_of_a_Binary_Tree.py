from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_map = dict[TreeNode, TreeNode]()
        parent_map[root] = None
        que = deque()
        que.append(root)
        stop_flag = 0 # stop if found the parents of both p and q
        while len(que) > 0:
            node_list = list[TreeNode]()
            while len(que) > 0:
                node = que.popleft()
                if node.left is not None:
                    node_list.append(node.left)
                    parent_map[node.left] = node
                    if node.left in [p, q]:
                        stop_flag += 1
                if node.right is not None:
                    node_list.append(node.right)
                    parent_map[node.right] = node
                    if node.right in [p, q]:
                        stop_flag += 1
            if stop_flag >= 2:
                break
            que.extend(node_list)

        parent_set = set[TreeNode]()
        node = p
        while node is not None:
            parent_set.add(node)
            node = parent_map[node]
        node = q
        while node is not None:
            if node in parent_set:
                return node
            node = parent_map[node]
        return None
