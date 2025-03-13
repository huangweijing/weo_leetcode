from typing import List
from collections import defaultdict
from functools import cache


class Solution:
    def __init__(self) -> None:
        self.children = defaultdict(lambda: set[int]())
        self.parents = []
        self.total_size = 0
        self.ans = 0
        self.max_score = 0
    
    @cache
    def tree_size(self, node: int) -> int:
        size = 1
        for child in self.children[node]:
            size += self.tree_size(child)
        return size
    
    def set_score(self, score: int):
        if score > self.max_score:
            self.max_score = score
            self.ans = 1
        elif score == self.max_score:
            self.ans += 1

    def my_sol(self, node: int):
        children = self.children[node]
        if len(children) == 0:
            self.set_score(self.total_size - 1)
        else:
            parent_size = self.total_size - 1
            size = 1
            for child in children:
                size *= self.tree_size(child)
                parent_size -= self.tree_size(child)
                self.my_sol(child)
            if self.parents[node] != -1:
                size *= parent_size
                # print(node, ":size=", size)
            self.set_score(size)
        
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        self.parents = parents
        for i, parent in enumerate(parents):
            self.children[parent].add(i)
        self.total_size = self.tree_size(0)
        # print(self.children, self.total_size)
        self.my_sol(0)
        return self.ans
    

data = [-1,2,0]
r = Solution().countHighestScoreNodes(data)
print(r)