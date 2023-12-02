from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        thief_list = [[i, j]
            for i, row in enumerate(grid)
            for j, col in enumerate(row) if col == 1
        ]
        safe_val_map = [[0] * n for _ in grid]
        visited = [[False] * n for _ in grid]
        for thief in thief_list:
            visited[thief[0]][thief[1]] = True
        cur = thief_list
        safe_val = 0
        while len(cur) > 0:
            new_cur = []
            while len(cur) > 0:
                pos = cur.pop()
                safe_val_map[pos[0]][pos[1]] = safe_val
                if pos[0] > 0 and not visited[pos[0] - 1][pos[1]]:
                    new_cur.append([pos[0] - 1, pos[1]])
                    visited[pos[0] - 1][pos[1]] = True
                if pos[1] > 0 and not visited[pos[0]][pos[1] - 1]:
                    new_cur.append([pos[0], pos[1] - 1])
                    visited[pos[0]][pos[1] - 1] = True
                if pos[0] < len(grid) - 1 and not visited[pos[0] + 1][pos[1]]:
                    new_cur.append([pos[0] + 1, pos[1]])
                    visited[pos[0] + 1][pos[1]] = True
                if pos[1] < len(grid) - 1 and not visited[pos[0]][pos[1] + 1]:
                    new_cur.append([pos[0], pos[1] + 1])
                    visited[pos[0]][pos[1] + 1] = True
            cur = new_cur
            safe_val += 1
        # print(safe_val_map)
        visited = [[False] * n for _ in grid]
        cur, next_cur, safe_val, visited[0][0] = [[0, 0]], [], safe_val_map[0][0], True
        while len(cur) > 0:
            # print(cur, safe_val, next_cur)
            pos = cur.pop()
            if pos == [n - 1, n - 1]:
                return safe_val
            if pos[0] > 0 and not visited[pos[0] - 1][pos[1]]:
                if safe_val_map[pos[0] - 1][pos[1]] >= safe_val:
                    cur.append([pos[0] - 1, pos[1]])
                elif safe_val_map[pos[0] - 1][pos[1]] == safe_val - 1:
                    next_cur.append([pos[0] - 1, pos[1]])
                visited[pos[0] - 1][pos[1]] = True
            if pos[1] > 0 and not visited[pos[0]][pos[1] - 1]:
                if safe_val_map[pos[0]][pos[1] - 1] >= safe_val:
                    cur.append([pos[0], pos[1] - 1])
                elif safe_val_map[pos[0]][pos[1] - 1] == safe_val - 1:
                    next_cur.append([pos[0], pos[1] - 1])
                visited[pos[0]][pos[1] - 1] = True
            if pos[0] < len(grid) - 1 and not visited[pos[0] + 1][pos[1]]:
                if safe_val_map[pos[0] + 1][pos[1]] >= safe_val:
                    cur.append([pos[0] + 1, pos[1]])
                elif safe_val_map[pos[0] + 1][pos[1]] == safe_val - 1:
                    next_cur.append([pos[0] + 1, pos[1]])
                visited[pos[0] + 1][pos[1]] = True
            if pos[1] < len(grid) - 1 and not visited[pos[0]][pos[1] + 1]:
                if safe_val_map[pos[0]][pos[1] + 1] >= safe_val:
                    cur.append([pos[0], pos[1] + 1])
                elif safe_val_map[pos[0]][pos[1] + 1] == safe_val - 1:
                    next_cur.append([pos[0], pos[1] + 1])
                visited[pos[0]][pos[1] + 1] = True
            if len(cur) == 0:
                cur = next_cur
                next_cur = []
                safe_val -= 1
        return -1



data = [[0,0,1],[0,1,1],[1,1,1]]
r = Solution().maximumSafenessFactor(data)
print(r)