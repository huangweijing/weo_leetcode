class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        elif n & 1 == 1:
            return n
        else:
            return n >> 1
