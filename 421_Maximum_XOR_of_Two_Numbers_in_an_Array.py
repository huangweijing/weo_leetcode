from typing import List

class TreeNode:
    def __init__(self):
        self.left: TreeNode = None
        self.right: TreeNode = None
        self.val: int = None

class BitTree:
    def __init__(self, bit_cnt: int):
        self.root: TreeNode = TreeNode()
        self.bit_cnt = bit_cnt

    def add(self, num: int):
        bit_num = self.bit_cnt
        cur = self.root
        while bit_num >= 0:
            bit = (num & (1 << bit_num)) >> bit_num
            bit_num -= 1
            if bit == 0:
                if cur.left is None:
                    cur.left = TreeNode()
                    cur.left.val = bit
                cur = cur.left
            elif bit == 1:
                if cur.right is None:
                    cur.right = TreeNode()
                    cur.right.val = bit
                cur = cur.right


    def best_num(self, num: int):
        bit_num = self.bit_cnt
        cur = self.root
        best_num = 0
        while bit_num >= 0:
            bit = (num & (1 << bit_num)) >> bit_num
            bit_num -= 1
            if bit == 0:
                if cur.right is not None:
                    cur = cur.right
                    best_num = (best_num << 1) | 1
                else:
                    cur = cur.left
                    best_num = (best_num << 1) | 0
            elif bit == 1:
                if cur.left is not None:
                    cur = cur.left
                    best_num = (best_num << 1) | 0
                else:
                    cur = cur.right
                    best_num = (best_num << 1) | 1
            # print(bit, best_num)
        return best_num


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_num = 0
        bt = BitTree(32)
        for num in nums:
            bt.add(num)
        for num in nums:
            n2 = bt.best_num(num)
            max_num = max(max_num, n2 ^ num)
        return max_num

r = Solution().findMaximumXOR([1, 2, 3])
print(r)