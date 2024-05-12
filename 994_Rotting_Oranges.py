from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        rotting_set = set[int]()
        fresh_set = set[int]()
        rotted_set = set[int]()
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 1:
                    fresh_set.add(i * n + j)
                elif col == 2:
                    rotting_set.add(i * n + j)
                    rotted_set.add(i * n + j)
        step_cnt = 0
        while len(fresh_set) > 0 and len(rotting_set) > 0:
            step_cnt += 1
            new_rotting_set = set[int]()
            while len(rotting_set) > 0:
                pos = rotting_set.pop()
                if pos + n in fresh_set:
                    fresh_set.remove(pos + n)
                    rotted_set.add(pos + n)
                    new_rotting_set.add(pos + n)
                if pos - n in fresh_set:
                    fresh_set.remove(pos - n)
                    rotted_set.add(pos - n)
                    new_rotting_set.add(pos - n)
                if pos % n != n - 1 and pos + 1 in fresh_set:
                    fresh_set.remove(pos + 1)
                    rotted_set.add(pos + 1)
                    new_rotting_set.add(pos + 1)
                if pos % n != 0 and pos - 1 in fresh_set:
                    fresh_set.remove(pos - 1)
                    rotted_set.add(pos - 1)
                    new_rotting_set.add(pos - 1)
            # print(fresh_set)
            rotting_set = new_rotting_set
        if len(fresh_set) > 0:
            return -1
        return step_cnt


grid = [[2,1,1],[1,1,0],[0,1,1]]
r = Solution().orangesRotting(grid)
print(r)

