from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[""] * n for _ in range(m)]
        for guard in guards:
            grid[guard[0]][guard[1]] = "g"
        for wall in walls:
            grid[wall[0]][wall[1]] = "w"
        for i in range(m):
            status = ""
            for j in range(n):
                if grid[i][j] == "g":
                    status = "*"
                elif grid[i][j] == "w":
                    status = ""
                elif grid[i][j] == "":
                    grid[i][j] = status
            status = ""
            for j in reversed(range(n)):
                if grid[i][j] == "g":
                    status = "*"
                elif grid[i][j] == "w":
                    status = ""
                elif grid[i][j] == "":
                    grid[i][j] = status


        for j in range(n):
            status = ""
            for i in range(m):
                if grid[i][j] == "g":
                    status = "*"
                elif grid[i][j] == "w":
                    status = ""
                elif grid[i][j] == "":
                    grid[i][j] = status
            for i in reversed(range(m)):
                if grid[i][j] == "g":
                    status = "*"
                elif grid[i][j] == "w":
                    status = ""
                elif grid[i][j] == "":
                    grid[i][j] = status
        ans = 0
        for row in grid:
            for val in row:
                if val == "":
                    ans += 1
        return ans


data = [
    4
    , 6
    , [[0,0],[1,1],[2,3]]
    , [[0,1],[2,2],[1,4]]
]
r = Solution().countUnguarded(* data)
print(r)
