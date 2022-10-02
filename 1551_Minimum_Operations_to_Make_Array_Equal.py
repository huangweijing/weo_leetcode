class Solution:
    def minOperations(self, n: int) -> int:
        cnt = n >> 1
        if n & 1 == 0:
            return ((n - 1 + 1) * cnt) >> 1
        else:
            return ((n - 1 + 0) * (cnt + 1)) >> 1
