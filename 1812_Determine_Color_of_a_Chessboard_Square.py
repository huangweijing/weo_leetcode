class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        row = ord(coordinates[0]) - ord("a")
        col = int(coordinates[1]) - 1
        return (row + col) & 1 != 0
