from typing import List


class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.val_dict = dict[int, list[int]]()
        self.grid = grid
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                self.val_dict[val] = [i, j]

    def adjacentSum(self, value: int) -> int:
        grid = self.grid
        pos = self.val_dict[value]
        sum_val = 0
        if pos[0] > 0:
            sum_val += grid[pos[0] - 1][pos[1]]
        if pos[0] < len(grid) - 1:
            sum_val += grid[pos[0] + 1][pos[1]]
        if pos[1] > 0:
            sum_val += grid[pos[0]][pos[1] - 1]
        if pos[1] < len(grid[0]) - 1:
            sum_val += grid[pos[0]][pos[1] + 1]
        return sum_val

    def diagonalSum(self, value: int) -> int:
        grid = self.grid
        pos = self.val_dict[value]
        sum_val = 0
        if pos[0] > 0 and pos[1] > 0:
            sum_val += grid[pos[0] - 1][pos[1] - 1]
        if pos[0] < len(grid) - 1 and pos[1] > 0:
            sum_val += grid[pos[0] + 1][pos[1] - 1]
        if pos[0] < len(grid) - 1 and pos[1] < len(grid[0]) - 1:
            sum_val += grid[pos[0] + 1][pos[1] + 1]
        if pos[0] > 0 and pos[1] < len(grid[0]) - 1:
            sum_val += grid[pos[0] - 1][pos[1] + 1]
        return sum_val



# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)