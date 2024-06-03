from typing import List
from collections import defaultdict
from functools import cache


class Solution:
    def __init__(self):
        self.nums = []
        self.k = 0
        self.children = defaultdict(lambda: set[int]())

    def construct_tree(self, edges: list[list[int]]):
        for edge in edges:
            self.children[edge[0]].add(edge[1])
            self.children[edge[1]].add(edge[0])
        parent_node = dict[int, int]()
        cur_nodes = set[int]([0])
        while len(cur_nodes) > 0:
            new_cur_nodes = []
            while len(cur_nodes) > 0:
                root = cur_nodes.pop()
                if root in parent_node:
                    # print(f"del {root}, {parent_node[root]}, {self.children[parent_node[root]]}")
                    self.children[root].remove(parent_node[root])
                for child in self.children[root]:
                    new_cur_nodes.append(child)
                    parent_node[child] = root
            cur_nodes = new_cur_nodes
        # print(self.children)

    @cache
    def my_sol(self, node: int, flip: bool) -> int:
        val = self.nums[node]
        if flip:
            odd_val, even_val = val, val ^ self.k
        else:
            odd_val, even_val = val ^ self.k, val
        if len(self.children[node]) == 0:
            # print(node, flip, even_val, self.nums[node])
            return even_val
        # if node == 0:
        #     print(f"detail:node={node},flip={flip}", odd_val, even_val)
        for i, child in enumerate(self.children[node]):
            flipped_val = self.my_sol(child, True)
            origin_val = self.my_sol(child, False)
            new_odd_val = max(odd_val + origin_val, even_val + flipped_val)
            new_even_val = max(odd_val + flipped_val, even_val + origin_val)
            odd_val, even_val = new_odd_val, new_even_val
            # if node == 0:
            #     print(f"detail:node={node},flip={flip}", child, flipped_val, origin_val, even_val)
        # print(node, flip, even_val, self.nums[node])
        return even_val

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        self.nums, self.k = nums, k
        self.construct_tree(edges)
        return self.my_sol(0, False)


data = [
    [0, 92, 56, 3, 34, 23, 56]
    , 7
    , [[2, 6], [4, 1], [5, 0], [1, 0], [3, 1], [6, 3]]
]
r = Solution().maximumValueSum(* data)
print(r)

print(bin(92), 92 ^ 7)
