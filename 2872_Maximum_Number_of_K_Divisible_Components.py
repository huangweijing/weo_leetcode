from typing import List
from collections import defaultdict
from functools import cache

class Solution:
    def __init__(self):
        self.values = []
        self.tree = defaultdict()
        self.k = 0
        self.tree_sum = []

    @cache
    def calc_sum(self, node: int) -> int:
        children = self.tree[node]
        sum_val = self.values[node]
        for child in children:
            sum_val += self.calc_sum(child)
        return sum_val

    @cache
    def my_sol(self, node: int) -> int:
        ret = 0
        children = self.tree[node]
        for child in children:
            if self.calc_sum(child) % self.k == 0:
                ret += 1
            ret += self.my_sol(child)
        return ret


    def maxKDivisibleComponents(self, n: int, edges: List[List[int]]
                                , values: List[int], k: int) -> int:
        adj_node_list = defaultdict(lambda : list[int]())
        children_nodes = defaultdict(lambda: list[int]())
        for edge in edges:
            adj_node_list[edge[0]].append(edge[1])
            adj_node_list[edge[1]].append(edge[0])
        stk = [[-1, 0]]
        while len(stk) > 0:
            new_stk = []
            while len(stk) > 0:
                node = stk.pop()
                adj_nodes = adj_node_list[node[1]]
                for adj in adj_nodes:
                    if adj != node[0]:
                        children_nodes[node[1]].append(adj)
                        new_stk.append([node[1], adj])
            stk = new_stk
        # print(children_nodes)
        self.tree = children_nodes
        self.k = k
        self.values = values
        return self.my_sol(0) + 1


data = [
7
, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
, [3,0,6,1,5,2,1]
, 3
]
r = Solution().maxKDivisibleComponents(* data)
print(r)





