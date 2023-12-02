import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(math.sqrt(c)) + 1):
            v = math.sqrt(c - i ** 2)
            if int(v) == v:
                return True
        return False
