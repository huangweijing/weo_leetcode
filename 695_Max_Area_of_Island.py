from typing import List

class Solution:
    def avail_pos(self, grid: list[list[int]], visited: list[list[bool]], start_pos:(int, int)) -> list[(int, int)]:
        result = []
        row_idx = start_pos[0]
        col_idx = start_pos[1]
        if row_idx - 1 >= 0:
            if grid[row_idx - 1][col_idx] == 1 and not visited[row_idx - 1][col_idx]:
                result.append((row_idx - 1, col_idx))
                visited[row_idx - 1][col_idx] = True
        if row_idx + 1 < len(grid):
            if grid[row_idx + 1][col_idx] == 1 and not visited[row_idx + 1][col_idx]:
                result.append((row_idx + 1, col_idx))
                visited[row_idx + 1][col_idx] = True
        if col_idx - 1 >= 0:
            if grid[row_idx][col_idx - 1] == 1 and not visited[row_idx][col_idx - 1]:
                result.append((row_idx, col_idx - 1))
                visited[row_idx][col_idx - 1] = True
        if col_idx + 1 < len(grid[0]):
            if grid[row_idx][col_idx + 1] == 1 and not visited[row_idx][col_idx + 1]:
                result.append((row_idx, col_idx + 1))
                visited[row_idx][col_idx + 1] = True
        return result

    def dfs(self, grid: List[List[int]], visited: List[List[int]], start_pos:(int, int)) -> int:
        if grid[start_pos[0]][start_pos[1]] == 0:
            return 0
        island_size = 0
        pos_list = [ start_pos ]
        visited[start_pos[0]][start_pos[1]] = True
        while len(pos_list) > 0:
            pos = pos_list.pop()
            # print(start_pos, pos_list, pos, island_size)
            # visited[pos[0]][pos[1]] = True
            island_size += 1
            pos_list.extend(self.avail_pos(grid, visited, pos))

        return island_size

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False] * len(grid[0]) for i in range(len(grid))]
        height = len(grid)
        width = len(grid[0])
        max_size = 0
        for row in range(height):
            for col in range(width):
                if grid[row][col] == 0:
                    continue
                if visited[row][col]:
                    continue

                island_size = self.dfs(grid, visited, (row, col))
                # print(row, col, island_size)
                if island_size > max_size:
                    max_size = island_size
        return max_size

r = Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
print(r)