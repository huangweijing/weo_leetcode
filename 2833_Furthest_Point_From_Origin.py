from collections import Counter


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cnt = Counter(moves)
        return abs(cnt["L"] - cnt["R"]) + cnt["_"]
