class Solution:
    def coloredCells(self, n: int) -> int:
        return ((n * (n - 1)) << 1) + 1