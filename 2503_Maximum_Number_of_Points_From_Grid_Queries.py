from typing import List
import heapq


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        my_queries = list(sorted(enumerate(queries), key=lambda x: [x[1], x[0]]))
        m, n = len(grid), len(grid[0])
        visited = set[int]([0])
        ans = []
        heap = [[grid[0][0], 0, 0]]
        size = 0
        for i, item in my_queries:
            while len(heap) > 0 and heap[0][0] < item:
                size += 1
                node = heapq.heappop(heap)
                if node[1] > 0:
                    node_id = (node[1] - 1) * n + node[2]
                    if node_id not in visited:
                        heapq.heappush(heap, [grid[node[1] - 1][node[2]], node[1] - 1, node[2]])
                        visited.add(node_id)
                if node[1] < m - 1:
                    node_id = (node[1] + 1) * n + node[2]
                    if node_id not in visited:
                        heapq.heappush(heap, [grid[node[1] + 1][node[2]], node[1] + 1, node[2]])
                        visited.add(node_id)
                if node[2] > 0:
                    node_id = node[1] * n + (node[2] - 1)
                    if node_id not in visited:
                        heapq.heappush(heap, [grid[node[1]][node[2] - 1], node[1], node[2] - 1])
                        visited.add(node_id)
                if node[2] < n - 1:
                    node_id = node[1] * n + (node[2] + 1)
                    if node_id not in visited:
                        heapq.heappush(heap, [grid[node[1]][node[2] + 1], node[1], node[2] + 1])
                        visited.add(node_id)
            ans.append([i, size])
            ans.sort()
        return [val[1] for val in ans]
    

data = [
    [[1,2,3],[2,5,7],[3,5,1]]
    , [5,6,2]
]
r = Solution().maxPoints(*data)
print(r)


                


