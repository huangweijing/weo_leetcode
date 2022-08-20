class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        t = 1
        while t <= n:
            if t == n:
                return True
            t <<= 2
        return False
