from typing import List
from collections import defaultdict
from functools import cache


class Solution:
    def __init__(self):
        self.child_nodes = defaultdict(lambda : list[int]())
        self.values = []

    @cache
    def calc_maximum_score(self, node: int) -> int:
        score1, score2 = 0, 0
        if len(self.child_nodes[node]) > 0:
            score2 = self.values[node]
        for child in self.child_nodes[node]:
            score1 += self.calc_sum_score(child)
            score2 += self.calc_maximum_score(child)
        return max(score1, score2)

    @cache
    def calc_sum_score(self, node: int) -> int:
        score = self.values[node]
        for child in self.child_nodes[node]:
            score += self.calc_sum_score(child)
        return score

    def maximumScoreAfterOperations(self, edges: List[List[int]]
                                    , values: List[int]) -> int:
        self.values = values
        connection = defaultdict(lambda : list[int]())
        for edge in edges:
            connection[edge[0]].append(edge[1])
            connection[edge[1]].append(edge[0])

        node_list = [(None, 0)]
        while len(node_list) > 0:
            parent, cur = node_list.pop()
            for next_node in connection[cur]:
                if next_node != parent:
                    self.child_nodes[cur].append(next_node)
                    node_list.append([cur, next_node])
        # print(self.child_nodes)
        return self.calc_maximum_score(0)

data = [
    [[7, 0], [3, 1], [6, 2], [4, 3], [4, 5], [4, 6], [4, 7]]
    , [2, 16, 23, 17, 22, 21, 8, 6]
]
sol = Solution()
r = sol.maximumScoreAfterOperations(* data)
print(r)
# print(sol.calc_sum_score(0))
# print(sol.calc_sum_score(2))
# print(sol.calc_sum_score(7))




