class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        for i in range(3, n + 1):
            t[i % 3] = sum(t)
        return t[n % 3]