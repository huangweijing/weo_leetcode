from functools import cache

class Solution:
    @cache
    def divisorGame(self, n: int) -> bool:
        for i in range(1, n):
            if n % i == 0:
                if not self.divisorGame(n - i):
                    return True
        return False
