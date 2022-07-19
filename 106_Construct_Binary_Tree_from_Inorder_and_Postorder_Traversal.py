# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def my_build_tree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1], None, None)
        for idx, num in enumerate(inorder):
            if root.val == num:
                root_idx = idx
                break
        # print(root_idx)
        left_inorder = inorder[: root_idx]
        right_inorder = inorder[root_idx + 1:]
        left_postorder = postorder[: len(left_inorder)]
        right_postorder = postorder[len(left_inorder): -1]
        # print(preorder, inorder, root_idx, left_preorder, left_inorder, right_preorder, right_inorder)
        root.left = self.my_build_tree(left_inorder, left_postorder)
        root.right = self.my_build_tree(right_inorder, right_postorder)
        return root


    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.my_build_tree(inorder, postorder)
