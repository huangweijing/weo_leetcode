from typing import List
from collections import deque

class Graph:
    def __init__(self, vertex_count: int):
        self.vertex_adj_list = [[] for x in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int):
        self.vertex_adj_list[v1].append(v2)
        # self.vertex_adj_list[v2].append(v1)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_vertex(self, v) -> list[int]:
        return self.vertex_adj_list[v]

class AlgorithmGetPathToBFS:
    def __init__(self, g: Graph):
        self.graph = g
        self.searched_mark = [0] * self.graph.get_vertex_count()
        self.path_length_arr = [-1] * self.graph.get_vertex_count()

    def get_path_to(self, start_vertex: int, end_vertex: int
                    , chrono_dict: dict[int, int]) -> int:
        self.searched_mark = [0] * self.graph.get_vertex_count()
        self.path_length_arr = [-1] * self.graph.get_vertex_count()
        self.searched_mark[start_vertex] = 1
        vertex_list = deque()
        vertex_list.append(start_vertex)
        path_length = 0
        while len(vertex_list) != 0:
            adj_vertex_list = []
            path_length += 1
            while len(vertex_list) != 0:
                v = vertex_list.pop()
                for adj_vertex in self.graph.get_adjacent_vertex(v):
                    if adj_vertex in chrono_dict:
                        adj_vertex = chrono_dict[adj_vertex]
                    if self.searched_mark[adj_vertex] == 0:
                        self.searched_mark[adj_vertex] = 1
                        self.path_length_arr[adj_vertex] = path_length
                        adj_vertex_list.append(adj_vertex)
            vertex_list = adj_vertex_list
        return self.path_length_arr[end_vertex]

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        g = Graph(n * n)
        for i in range(0, n * n):
            for j in range(1, 7):
                if i + j < n * n:
                    g.add_edge(i, i + j)
        # print([[idx, val] for idx, val in enumerate(g.vertex_adj_list)])
        node_id = 0
        row, col = n - 1, 0
        col_increment = 1
        chrono_dict = dict[int, int]()
        while node_id < n * n:
            # print(row, col)
            if board[row][col] != -1:
                chrono_dict[node_id] = board[row][col] - 1
            if col == n - 1 and col_increment == 1:
                row -= 1
                col_increment = 0
            elif col == n - 1 and col_increment == 0:
                col_increment = -1
            elif col == 0 and col_increment == -1:
                row -= 1
                col_increment = 0
            elif col == 0 and col_increment == 0:
                col_increment = 1
            node_id += 1
            col += col_increment
        # print(chrono_dict)
        alg = AlgorithmGetPathToBFS(g)
        path = alg.get_path_to(0, n * n - 1, chrono_dict)
        # print(path)
        return path

data = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
r = Solution().snakesAndLadders(data)
print(r)