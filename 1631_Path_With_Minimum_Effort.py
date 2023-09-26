import heapq
import math
from typing import List

class Diff:
    def __init__(self, row_idx: int, col_idx: int, max_diff: int):
        self.row_idx = row_idx
        self.col_idx = col_idx
        self.max_diff = max_diff

    def __lt__(self, other):
        return self.max_diff < other.max_diff

    def __str__(self):
        return f"row_idx={self.row_idx}, col_idx={self.col_idx}, self.max_diff={self.max_diff}"

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dp = [[math.inf] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        dp[0][0] = 0
        node_list = [Diff(0, 0, 0)]
        while dp[m - 1][n - 1] == math.inf:
            node = heapq.heappop(node_list)
            visited[node.row_idx][node.col_idx] = True
            dp[node.row_idx][node.col_idx] = min(dp[node.row_idx][node.col_idx], node.max_diff)
            if node.row_idx - 1 >= 0:
                diff = abs(heights[node.row_idx][node.col_idx] - heights[node.row_idx - 1][node.col_idx])
                diff_obj = Diff(node.row_idx - 1, node.col_idx, max(diff, dp[node.row_idx][node.col_idx]))
                if not visited[diff_obj.row_idx][diff_obj.col_idx]:
                    heapq.heappush(node_list, diff_obj)
            if node.row_idx + 1 < m:
                diff = abs(heights[node.row_idx][node.col_idx] - heights[node.row_idx + 1][node.col_idx])
                diff_obj = Diff(node.row_idx + 1, node.col_idx, max(diff, dp[node.row_idx][node.col_idx]))
                if not visited[diff_obj.row_idx][diff_obj.col_idx]:
                    heapq.heappush(node_list, diff_obj)
            if node.col_idx - 1 >= 0:
                diff = abs(heights[node.row_idx][node.col_idx] - heights[node.row_idx][node.col_idx - 1])
                diff_obj = Diff(node.row_idx, node.col_idx - 1, max(diff, dp[node.row_idx][node.col_idx]))
                if not visited[diff_obj.row_idx][diff_obj.col_idx]:
                    heapq.heappush(node_list, diff_obj)
            if node.col_idx + 1 < n:
                diff = abs(heights[node.row_idx][node.col_idx] - heights[node.row_idx][node.col_idx + 1])
                diff_obj = Diff(node.row_idx, node.col_idx + 1, max(diff, dp[node.row_idx][node.col_idx]))
                if not visited[diff_obj.row_idx][diff_obj.col_idx]:
                    heapq.heappush(node_list, diff_obj)
            # print(dp)
            # print(list(map(str, node_list)))
        return dp[m - 1][n - 1]


data = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
r = Solution().minimumEffortPath(data)
print(r)





