class Solution:
    def can_part(self, n: int, sqr: int) -> bool:
        if n == sqr:
            return True
        if sqr < n:
            return False
        mod = 10
        rem = sqr % mod
        while rem <= n:
            if self.can_part(n - rem, sqr // mod):
                return True
            mod *= 10
            rem = sqr % mod
        return False

    def punishmentNumber(self, n: int) -> int:
        return sum(i ** 2 for i in range(1, n + 1)
                   if self.can_part(i, i ** 2))

r = Solution().punishmentNumber(37)
print(r)