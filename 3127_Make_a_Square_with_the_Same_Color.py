class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(2):
            for j in range(2):
                w, b = 0, 0
                for k in range(i, i + 2):
                    for l in range(j, j + 2):
                        if grid[k][l] == "W":
                            w += 1
                        else:
                            b += 1
                if w != b != 2:
                    return True
        return False

