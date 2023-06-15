from typing import List
from collections import defaultdict


class Solution:
    def __init__(self):
        self.head_id = -1
        self.children = defaultdict(lambda : list[int]())
        self.inform_time = []
        self.ans = 0

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # children = defaultdict(lambda : list[int]())
        self.head_id = headID
        self.inform_time = informTime
        for i in range(len(manager)):
            self.children[manager[i]].append(i)
        self.inform(headID, 0)
        return self.ans

    def inform(self, root: int, used_time):
        self.ans = max(self.ans, used_time)
        children = self.children[root]
        for child in children:
            self.inform(child, used_time + self.inform_time[root])


data = [
    6
    , 2
    , [2, 2, -1, 2, 2, 2]
    , [0, 0, 1, 0, 0, 0]
]
r = Solution().numOfMinutes(* data)
print(r)