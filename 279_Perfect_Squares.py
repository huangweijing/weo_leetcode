import math

class Solution:
    def __init__(self):
        self.min_arr = []

    def numSquares(self, n: int) -> int:
        self.min_arr = [400] * (n + 1)
        self.min_arr[0] = 0
        t = int(math.sqrt(n)) + 1

        for j in range(1, t):
            square = j ** 2
            for i in range(square, n + 1):
                self.min_arr[i] = min(self.min_arr[i], self.min_arr[i - square] + 1)

        return self.min_arr[n]

r = Solution().numSquares(9999)
print(r)


