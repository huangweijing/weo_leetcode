from typing import List
from collections import deque

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
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        entrance_key = entrance[0] * n + entrance[1]
        exit_arr = []
        g = Graph(m * n)
        for i in range(m):
            for j in range(n):
                key = i * n + j
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and maze[i][j] == "." and key != entrance_key:
                    exit_arr.append(key)
                if maze[i][j] != ".":
                    continue
                if j - 1 >= 0 and maze[i][j - 1] == ".":
                    g.add_edge(key, i * n + j - 1)
                    pass
                if i - 1 >= 0 and maze[i - 1][j] == ".":
                    g.add_edge(key, (i - 1) * n + j)
                    pass
                if j + 1 < n and maze[i][j + 1] == ".":
                    g.add_edge(key, i * n + j + 1)
                    pass
                if i + 1 < m and maze[i + 1][j] == ".":
                    g.add_edge(key, (i + 1)* n + j)
                    pass
        step_cnt_arr = [-1] * (m * n)
        q = set[int]()
        step_cnt = 1
        q.add(entrance_key)
        step_cnt_arr[entrance_key] = 0
        while len(q) > 0:
            # print(q, step_cnt_arr, exit_arr)
            new_q = set[int]()
            while len(q) > 0:
                v = q.pop()
                adj_vertices = g.get_adjacent_vertex(v)
                for adj in adj_vertices:
                    if step_cnt_arr[adj] != -1:
                        continue
                    step_cnt_arr[adj] = step_cnt
                    new_q.add(adj)
            step_cnt += 1
            q = new_q
        ans = m * n + 1
        for exit_pos in exit_arr:
            if step_cnt_arr[exit_pos] == -1:
                continue
            # print(ans)
            ans = min(step_cnt_arr[exit_pos], ans)
        if ans == m * n + 1:
            return -1
        return ans

data =[[["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
, [1,2]]
r = Solution().nearestExit(* data)
print(r)