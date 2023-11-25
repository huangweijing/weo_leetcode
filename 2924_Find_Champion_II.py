from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        prev_nodes = defaultdict(lambda : list[int]())
        for edge in edges:
            prev_nodes[edge[1]].append(edge[0])
        first_set = set()
        for i in range(n):
            if len(prev_nodes[i]) == 0:
                first_set.add(i)
        if len(first_set) == 1:
            return first_set.pop()
        else:
            return -1
