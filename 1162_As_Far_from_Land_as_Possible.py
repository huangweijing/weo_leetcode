from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        land_list = list[list[int]]()
        visited_set = set()
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    land_list.append([row, col])
                    visited_set.add(row * 101 + col)
        ans = 0
        if len(land_list) in (0, n * n) :
            return -1
        while len(land_list) > 0:
            new_land_list = []
            while len(land_list) > 0:
                p = land_list.pop()
                new_point = [[p[0] - 1, p[1]], [p[0] + 1, p[1]]
                    , [p[0], p[1] - 1], [p[0], p[1] + 1]]
                for point in new_point:
                    if point[0] < 0 or point[0] >= n or point[1] < 0 or point[1] >= n:
                        continue
                    if point[0] * 101 + point[1] not in visited_set:
                        visited_set.add(point[0] * 101 + point[1])
                        new_land_list.append(point)
            land_list = new_land_list
            if len(land_list) == 0:
                return ans
            ans += 1
        return ans

data = [[1,0,1],[0,0,0],[0,0,0]]
r = Solution().maxDistance(data)
print(r)

