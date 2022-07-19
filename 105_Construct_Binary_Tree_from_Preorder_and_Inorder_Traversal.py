from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.inorder_hash = dict[int, int]()

    def my_build_tree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0], None, None)
        for idx, num in enumerate(inorder):
            if root.val == num:
                root_idx = idx
                break
        # print(root_idx)
        left_inorder = inorder[: root_idx]
        right_inorder = inorder[root_idx + 1:]
        left_preorder = preorder[1: len(left_inorder) + 1]
        right_preorder = preorder[len(left_inorder) + 1:]
        # print(preorder, inorder, root_idx, left_preorder, left_inorder, right_preorder, right_inorder)
        root.left = self.my_build_tree(left_preorder, left_inorder)
        root.right = self.my_build_tree(right_preorder, right_inorder)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # for idx, val in enumerate(inorder):
        #     self.inorder_hash[val] = idx
        return self.my_build_tree(preorder, inorder)

preorder_data = [3,9,20,15,7]
inorder_data = [9,3,15,20,7]
# preorder_data = [-1]
# inorder_data = [-1]
node = Solution().buildTree(preorder_data, inorder_data)
print(node.val, node.left, node.right)