class Solution:
    def isPathCrossing(self, path: str) -> bool:
        mod = 10 ** 5
        pos = 0
        pos_set = set[int]([pos])
        for ch in path:
            if ch == "E":
                pos += 1
            elif ch == "W":
                pos -= 1
            elif ch == "N":
                pos += mod
            elif ch == "S":
                pos -= mod
            if pos in pos_set:
                return True
            pos_set.add(pos)
        return False

