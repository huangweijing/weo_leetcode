from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        visited = [[0] * len(land[0]) for _ in land ]
        def dfs(pos: (int, int)) -> list[int]:
            if visited[pos[0]][pos[1]] == 1:
                return pos
            visited[pos[0]][pos[1]] = 1
            ret = list(pos)
            if pos[0] - 1 >= 0 and visited[pos[0] - 1][pos[1]] == 0 and land[pos[0] - 1][pos[1]] == 1:
                br = dfs((pos[0] - 1, pos[1]))
                if br is not None:
                    ret[0], ret[1] = max(ret[0], br[0]), max(ret[1], br[1])
            if pos[0] + 1 < len(land) and visited[pos[0] + 1][pos[1]] < len(land) and land[pos[0] + 1][pos[1]] == 1:
                br = dfs((pos[0] + 1, pos[1]))
                if br is not None:
                    ret[0], ret[1] = max(ret[0], br[0]), max(ret[1], br[1])
            if pos[1] - 1 >= 0 and visited[pos[0]][pos[1] - 1] >= 0 and land[pos[0]][pos[1] - 1] == 1:
                br = dfs((pos[0], pos[1] - 1))
                if br is not None:
                    ret[0], ret[1] = max(ret[0], br[0]), max(ret[1], br[1])
            if pos[1] + 1 < len(land[0]) and visited[pos[0]][pos[1] + 1] < len(land[0]) and land[pos[0]][pos[1] + 1] == 1:
                br = dfs((pos[0], pos[1] + 1))
                if br is not None:
                    ret[0], ret[1] = max(ret[0], br[0]), max(ret[1], br[1])
            return ret
        ans = []
        for i, row in enumerate(land):
            for j, val in enumerate(row):
                if land[i][j] == 0:
                    continue
                if visited[i][j] == 1:
                    continue
                br = dfs((i, j))
                ans.append([i, j, br[0], br[1]])
        return ans

land = [[1,0,0],[0,1,1],[0,1,1]]
r = Solution().findFarmland(land)
print(r)

