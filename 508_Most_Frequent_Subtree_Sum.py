from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.sum_dict = dict[int, int]()

    def traverse_sum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        result = root.val
        if root.left is not None:
            result += self.traverse_sum(root.left)
        if root.right is not None:
            result += self.traverse_sum(root.right)
        if result not in self.sum_dict.keys():
            self.sum_dict[result] = 0
        self.sum_dict[result] += 1
        return result

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse_sum(root)
        max_freq = 0
        freq_rank = list[int]()
        for key in self.sum_dict.keys():
            freq = self.sum_dict[key]
            if freq > max_freq:
                freq_rank = list[int]()
                max_freq = freq
            if freq == max_freq:
                freq_rank.append(key)
        return freq_rank

