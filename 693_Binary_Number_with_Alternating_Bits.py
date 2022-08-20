class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = n & 1
        n = n >> 1
        while n > 0:
            if (b ^ (n & 1)) == 0:
                return False
            b = n & 1
            n >>= 1
        return True
