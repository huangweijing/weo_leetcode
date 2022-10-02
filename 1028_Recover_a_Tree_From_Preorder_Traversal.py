from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.level_dict = {}
        self.cur_idx = 0

    def make_tree(self, level_list: list[int], num_list: list[int]) -> TreeNode:
        root = TreeNode(val=num_list[self.cur_idx])
        root_level = level_list[self.cur_idx]
        # print(f"root.val={num_list[self.cur_idx]}, root.level={level_list[self.cur_idx]}, cur={self.cur_idx}")
        self.cur_idx += 1
        if self.cur_idx >= len(level_list):
            return root
        if level_list[self.cur_idx] == root_level + 1:
            root.left = self.make_tree(level_list, num_list)
        if self.cur_idx >= len(level_list):
            return root
        if level_list[self.cur_idx] == root_level + 1:
            root.right = self.make_tree(level_list, num_list)
        return root


    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        level_list = []
        num_list = []
        i = 0
        while i < len(traversal):
            level = 0
            while i < len(traversal) and traversal[i] == "-":
                level += 1
                i += 1
            level_list.append(level)
            num = 0
            while i < len(traversal) and traversal[i] != "-":
                num = num * 10 + ord(traversal[i]) - ord("0")
                i += 1
            num_list.append(num)
            # print(f"level={level}, num={num}, i={i}")
        # print(level_list)
        # print(num_list)
        return self.make_tree(level_list, num_list)

data_traversal = "1-2--3---4-5--6---7"
r = Solution().recoverFromPreorder(data_traversal)
print(r)
