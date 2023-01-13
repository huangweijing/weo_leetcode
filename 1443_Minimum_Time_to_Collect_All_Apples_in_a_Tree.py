from typing import List


class Graph:
    def __init__(self, vertex_count: int):
        self.vertex_adj_list = [[] for x in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int):
        self.vertex_adj_list[v1].append(v2)
        self.vertex_adj_list[v2].append(v1)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_vertex(self, v) -> list[int]:
        return self.vertex_adj_list[v]

class Solution:
    def __init__(self):
        self.hasApple = []

    def my_sol(self, parent: int, root: int, g: Graph) -> (bool, int):
        v_list = g.get_adjacent_vertex(root)
        cur_has_apple = self.hasApple[root]
        ans = 0
        for v in v_list:
            if v == parent:
                continue
            sub_apple, sub_time = self.my_sol(root, v, g)
            if sub_apple:
                cur_has_apple = True
                ans += sub_time + 2
        return cur_has_apple, ans

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.hasApple = hasApple
        g = Graph(n)
        for edge in edges:
            g.add_edge(edge[0], edge[1])
        apple, time = self.my_sol(None, 0, g)
        return time

true, false = True, False
data = [
    7
    , [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    , [false,false,true,false,false,true,false]
]
r = Solution().minTime(* data)
print(r)



