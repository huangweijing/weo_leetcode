from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.preorder = []
        self.postorder = []
        self.preorder_dict = dict[int, int]()
        self.postorder_dict = dict[int, int]()

    def my_tree(self, pre_sta:int, pre_end: int, pos_sta: int, pos_end: int) -> TreeNode:
        # print(pre_sta, pre_end, pos_sta, pos_end, self.preorder[pre_sta: pre_end + 1], self.postorder[pos_sta: pos_end + 1])
        val = self.preorder[pre_sta]
        root = TreeNode(val=val, left=None, right=None)
        if pre_sta == pre_end:
            return root
        # only have left child or right child
        if self.postorder[pos_end - 1] == self.preorder[pre_sta + 1]:
            root.left = self.my_tree(pre_sta + 1, pre_end, pos_sta, pos_end - 1)
            return root

        left_root_val = self.preorder[pre_sta + 1]
        left_tree_post_sta = pos_sta
        left_tree_post_end = self.postorder_dict[left_root_val]
        right_tree_post_sta = left_tree_post_end + 1
        right_tree_post_end = pos_end - 1

        left_tree_pre_sta = pre_sta + 1
        left_tree_pre_end = pre_sta + 1 + left_tree_post_end - left_tree_post_sta
        right_tree_pre_sta = left_tree_pre_end + 1
        right_tree_pre_end = pre_end

        root.left = self.my_tree(left_tree_pre_sta, left_tree_pre_end
                                 , left_tree_post_sta, left_tree_post_end)
        root.right = self.my_tree(right_tree_pre_sta, right_tree_pre_end
                                 , right_tree_post_sta, right_tree_post_end)
        return root

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.preorder, self.postorder = preorder, postorder
        for i, item in enumerate(preorder):
            self.preorder_dict[item] = i
        for i, item in enumerate(postorder):
            self.postorder_dict[item] = i
        return self.my_tree(0, len(preorder) - 1, 0, len(postorder) - 1)

data = [
[2,1]
, [1,2]
]
Solution().constructFromPrePost(* data)