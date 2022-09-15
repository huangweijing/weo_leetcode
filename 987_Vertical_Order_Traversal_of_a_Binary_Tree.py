from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.vertical_dict = dict[int, dict[int, list[TreeNode]]]()

    def my_vertical_traversal(self, root: TreeNode, root_pos: list[int]):
        if root is None:
            return
        if root_pos[1] not in self.vertical_dict:
            self.vertical_dict[root_pos[1]] = dict[int, list[TreeNode]]()
        if root_pos[0] not in self.vertical_dict[root_pos[1]]:
            self.vertical_dict[root_pos[1]][root_pos[0]] = list[int]()
        self.vertical_dict[root_pos[1]][root_pos[0]].append(root.val)

        if root.left is not None:
            self.my_vertical_traversal(root.left, [root_pos[0] + 1, root_pos[1] - 1])
        if root.right is not None:
            self.my_vertical_traversal(root.right, [root_pos[0] + 1, root_pos[1] + 1])

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.my_vertical_traversal(root, [0, 0])
        result = []
        key_list = list(self.vertical_dict.keys())
        key_list.sort()
        # print(key_list)
        for key in key_list:
            ver_val_list = []
            ver_key_list = list(self.vertical_dict[key].keys())
            # print(ver_key_list)
            ver_key_list.sort()
            for ver_key in ver_key_list:
                self.vertical_dict[key][ver_key].sort()
                ver_val_list.extend(self.vertical_dict[key][ver_key])
            result.append(ver_val_list)
        return result

