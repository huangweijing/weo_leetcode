from typing import List

class Graph:
    def __init__(self, vertex_count: int):
        self.vertex_adj_list = [[] for _ in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int):
        self.vertex_adj_list[v1].append(v2)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_vertex(self, v) -> list[int]:
        return self.vertex_adj_list[v]

    def count(self, v) -> int:
        v_list = [v]
        visited = set[int](v_list)
        while len(v_list) > 0:
            cur = v_list.pop()
            adj_list = self.vertex_adj_list[cur]
            for next_v in adj_list:
                if next_v not in visited:
                    visited.add(next_v)
                    v_list.append(next_v)
        return len(visited)


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        g = Graph(len(bombs))
        ans = 0
        for i in range(len(bombs)):
            bomb1 = bombs[i]
            x1 = bomb1[0]
            y1 = bomb1[1]
            r1 = bomb1[2]
            for j in range(len(bombs)):
                if i == j:
                    continue
                bomb2 = bombs[j]
                x2 = bomb2[0]
                y2 = bomb2[1]
                # print(x1, x2, y1, y2, r1)
                # print((x1 - x2) ** 2 + (y1 - y2) ** 2, r1 ** 2)
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 ** 2:
                    # print(f"{i} -> {j}")
                    g.add_edge(i, j)

        for i in range(len(bombs)):
            ans = max(ans, g.count(i))

        return ans

data = [[2,1,3],[6,1,4]]

r = Solution().maximumDetonation(data)
print(r)