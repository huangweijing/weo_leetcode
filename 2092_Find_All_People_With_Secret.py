from typing import List
from collections import defaultdict


class Graph:
    def __init__(self):
        self.vertex_adj_list = defaultdict(lambda: set[int]())
        self.edge_count = 0
        self.vertex_count = 0

    def add_edge(self, v1: int, v2: int):
        self.vertex_adj_list[v1].add(v2)
        self.vertex_adj_list[v2].add(v1)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_vertex(self, v) -> set[int]:
        return self.vertex_adj_list[v]


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        know_secret = [False] * n
        meetings.sort(key=lambda x: x[2])
        time, know_secret[firstPerson], know_secret[0] = 0, True, True
        idx = 0
        while idx < len(meetings):
            m = meetings[idx]
            know_set = set[int]()
            sub_set_cnt = 0
            tmp_idx = idx
            while idx < len(meetings) and meetings[idx][2] == m[2]:
                if know_secret[meetings[idx][0]]:
                    know_set.add(meetings[idx][0])
                if know_secret[meetings[idx][1]]:
                    know_set.add(meetings[idx][1])
                sub_set_cnt += 1
                idx += 1
            visited = set[int]()
            g = Graph()
            idx = tmp_idx
            while idx < len(meetings) and meetings[idx][2] == m[2]:
                g.add_edge(meetings[idx][0], meetings[idx][1])
                idx += 1
            for p in know_set:
                visited.add(p)
            next_set = know_set
            while len(next_set) > 0:
                new_next_set = set[int]()
                for node in next_set:
                    for adj in g.get_adjacent_vertex(node):
                        if adj in visited:
                            continue
                        know_secret[adj] = True
                        visited.add(adj)
                        new_next_set.add(adj)
                next_set = new_next_set

        return [i for i, p in enumerate(know_secret) if p]


data = [
    6
, [[0,2,1],[1,3,1],[4,5,1]]
, 1
]
r = Solution().findAllPeople(* data)
print(r)

