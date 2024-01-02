class Solution:
    def minOperations(self, s: str) -> int:
        a1 = sum(1 if (ch == "1" and i & 1 == 0) or (ch == "0" and i & 1 == 1)
                 else 0 for i, ch in enumerate(s))
        a2 = len(s) - a1
        return min(a1, a2)
