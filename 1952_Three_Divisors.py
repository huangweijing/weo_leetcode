from math import sqrt

class Solution:
    def is_prime(self, n: int) -> bool:
        if n < 2:
            return False
        max_num = int(sqrt(n))
        for i in range(2, max_num + 1):
            if n % i == 0:
                return False
        return True

    def isThree(self, n: int) -> bool:
        if n == 1:
            return False
        sqrt_n = sqrt(n)
        return sqrt_n == int(sqrt_n) and self.is_prime(int(sqrt_n))
