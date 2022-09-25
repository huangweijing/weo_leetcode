class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n & 1 == 0 else n << 1
