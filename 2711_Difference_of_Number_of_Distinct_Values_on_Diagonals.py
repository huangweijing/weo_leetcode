from typing import List
from collections import Counter


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            cnt = Counter()
            pos_stk = []
            step = 0
            while i + step < m and step < n:
                pos_stk.append([i + step, step])
                ans[i + step][step] = len(cnt)
                cnt[grid[i + step][step]] += 1
                step += 1
            cnt = Counter()
            while len(pos_stk) > 0:
                pos = pos_stk.pop()
                ans[pos[0]][pos[1]] = abs(ans[pos[0]][pos[1]] - len(cnt))
                cnt[grid[pos[0]][pos[1]]] += 1

        for i in range(1, n):
            cnt = Counter()
            pos_stk = []
            step = 0
            while step < m and i + step < n:
                pos_stk.append([step, i + step])
                ans[step][i + step] = len(cnt)
                cnt[grid[step][i + step]] += 1
                step += 1
            cnt = Counter()
            while len(pos_stk) > 0:
                pos = pos_stk.pop()
                ans[pos[0]][pos[1]] = abs(ans[pos[0]][pos[1]] - len(cnt))
                cnt[grid[pos[0]][pos[1]]] += 1

        return ans

data = [
[[6,28,37,34,12,30,43,35,6],[21,47,38,14,31,49,11,14,49],[6,12,35,17,17,2,45,27,43],[34,41,30,28,45,24,50,20,4]]
]
r = Solution().differenceOfDistinctValues(* data)
print(r)

