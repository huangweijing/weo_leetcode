from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        nodes = []
        visited = set[int]()
        m, n = len(isWater), len(isWater[0])
        height_dict = dict[int, int]()
        for i, row in enumerate(isWater):
            for j, val in enumerate(row):
                if val == 1:
                    nodes.append([i, j])
                    visited.add(i * n + j)
                    height_dict[i * n + j] = 0
        height = 0
        while len(nodes) > 0:
            next_nodes = []
            while len(nodes) > 0:
                node = nodes.pop()
                offsets = [[1, 0], [0, 1], [0, -1], [-1, 0]]
                for offset in offsets:
                    next_node = [node[0] + offset[0], node[1] + offset[1]]
                    if not (0 <= next_node[0] < m and 0 <= next_node[1] < n):
                        continue
                    if next_node[0] * n + next_node[1] in visited:
                        continue
                    visited.add(next_node[0] * n + next_node[1])
                    height_dict[next_node[0] * n + next_node[1]] = height + 1
                    next_nodes.append(next_node)
            nodes = next_nodes
            height += 1
        ans = [[0] * n for _ in range(m)]
        for key in height_dict:
            ans[key // n][key % n] = height_dict[key]
        return ans


data = [[0,0],[1,1],[1,0]]
r = Solution().highestPeak(data)
print(r)