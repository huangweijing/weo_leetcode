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
        self.g = Graph(1)
        self.s = ""
        self.visited = []
        
    def my_sol(self, parent:int, root: int) -> (int, int):
        # print(root)
        height_list, longest_path = [], 0
        adj_vertex_list = self.g.get_adjacent_vertex(root)
        for adj_vertex in adj_vertex_list:
            if adj_vertex == parent:
                continue
            sub_height, sub_longest_path = self.my_sol(root, adj_vertex)
            height_list.append(sub_height)
            longest_path = max(sub_longest_path, longest_path)
        height_list.sort(reverse=True)
        # print(height_list)
        if len(height_list) == 0:
            longest_path = 1
            height = 1
        elif len(height_list) == 1:
            longest_path = max(height_list[0] + 1, longest_path)
            height = height_list[0] + 1
        else:
            longest_path = max(height_list[0] + height_list[1] + 1, longest_path)
            height = height_list[0] + 1
        self.visited[root] = True
        # print(root, height, longest_path)
        return height, longest_path


    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        self.visited = [False] * n
        self.s = s
        self.g = Graph(n)
        for i, p in enumerate(parent):
            if p == -1:
                continue
            if self.s[i] != s[p]:
                self.g.add_edge(i, p)
        # print(self.g.vertex_adj_list)
        ans = 0
        for i in range(n):
            if not self.visited[i]:
                _, path = self.my_sol(None, i)
                # print(i, path)
                ans = max(ans, path)
        return ans

data = [
    [-1,0,0,1,1,2]
    , "abacbe"
]
r = Solution().longestPath(* data)
print(r)
