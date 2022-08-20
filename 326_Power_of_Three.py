class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 0
        while 3 ** i <= abs(n):
            if 3 ** i == n:
                return True
            i += 1
        return False
