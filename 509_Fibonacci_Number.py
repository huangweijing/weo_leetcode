class Solution:
    def __init__(self):
        self.dp = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]
        # self.dp[0] = 0
        # self.dp[1] = 1

    def fib(self, n: int) -> int:
        if self.dp[n] is not None:
            return self.dp[n]

        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dp[n]

# for i in range(31):
#     r = Solution().fib(8)
#     print(r)

r = map(Solution().fib, list(range(31)))
print(list(r))

