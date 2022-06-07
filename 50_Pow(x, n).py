class Solution:
    def __init__(self):
        self.cache: List[int] = [None] * 100000

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x
        return self.my_cache_pow(x, n)

    def my_cache_pow(self, x: float, n: int) -> float:
        if n < len(self.cache) and self.cache[n] is not None:
            return self.cache[n]
        if n == 0:
            return 1
        if n == 1:
            return x
        if n & 1 == 0:
            r = self.my_cache_pow(x, n >> 1)
            result = r * r
        else:
            r = self.my_cache_pow(x, n >> 1)
            result = r * r * x
        if n < len(self.cache):
            self.cache[n] = result
        return result

sol = Solution()
print(sol.myPow(1.00001, 123456))

