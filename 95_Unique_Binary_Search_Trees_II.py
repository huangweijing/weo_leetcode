from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generate_tree(self, arr: list[int]) -> list[TreeNode]:
        if len(arr) == 0:
            return None
        if len(arr) == 1:
            return [TreeNode(val=arr[0], left=None, right=None)]

        result = list[TreeNode]()
        for i in range(len(arr)):
            left_node_list = self.generate_tree(arr[: i])
            right_node_list = self.generate_tree(arr[i + 1: ])
            if left_node_list is None and right_node_list is None:
                root = TreeNode(val=arr[i], left=None, right=None)
                result.append(root)
            elif left_node_list is None:
                for right_node in right_node_list:
                    root = TreeNode(val=arr[i], left=None, right=right_node)
                    result.append(root)
            elif right_node_list is None:
                for left_node in left_node_list:
                    root = TreeNode(val=arr[i], left=left_node, right=None)
                    result.append(root)
            else:
                for left_node in left_node_list:
                    for right_node in right_node_list:
                        root = TreeNode(val=arr[i], left=left_node, right=right_node)
                        result.append(root)
        return result

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        result = self.generate_tree(list(range(1, n+1)))
        return result

r = Solution().generateTrees(1)
print(len(r))