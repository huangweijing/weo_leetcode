from collections import Counter


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = Counter(s)
        return (cnt["1"] - 1) * "1" + cnt["0"] * "0" + "1"
