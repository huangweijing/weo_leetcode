from typing import List
from collections import defaultdict


class Solution:
    def __init__(self) -> None:
        self.parent = []
        self.s = ""
        self.children = defaultdict(lambda: set[int]())

    def my_sol(self, node: int, alp_ans: dict[str, int]):
        children = self.children[node]
        ch = self.s[node]
        if ch in alp_ans:
            ans_node = alp_ans[ch]
            cur_parent = self.parent[node]
            if cur_parent != -1:
                self.children[cur_parent].remove(node)
            self.parent[node] = ans_node
            self.children[ans_node].add(node)
        new_alp_ans = alp_ans.copy()
        new_alp_ans[ch] = node
        for child in children.copy():
            self.my_sol(child, new_alp_ans)


    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        self.parent, self.s = parent, s
        for node in range(len(parent)):
            if parent[node] != -1:
                p = parent[node]
                self.children[p].add(node)
        # print(self.children)
        self.my_sol(0, dict[str, int]())
        # print(self.children)
        sizes = [0] * len(parent)
        def get_size(node: int) -> int:
            size = 1
            for child in self.children[node]:
                size += get_size(child)
            sizes[node] = size
            return size
        get_size(0)
        return sizes
    

data = [
    [-1,0,0,1,1,1]
    , "abaabc"
]
r = Solution().findSubtreeSizes(*data)
print(r)