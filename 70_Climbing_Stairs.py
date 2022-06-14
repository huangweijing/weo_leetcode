class Solution:
    def __init__(self):
        self.solution: list[int] = [None] * 50
        self.solution[1] = 1
        self.solution[2] = 2

    def climbStairs(self, n: int) -> int:

        if self.solution[n] is not None:
            return self.solution[n]

        self.solution[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.solution[n]
