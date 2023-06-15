from typing import List
from functools import cache

class Solution:
    def __init__(self):
        self.questions = []

    @cache
    def my_sol(self, pos: int) -> int:
        if pos >= len(self.questions):
            return 0
        p1 = self.questions[pos][0] + self.my_sol(pos + self.questions[pos][1] + 1)
        p2 = self.my_sol(pos + 1)
        return max(p1, p2)

    def mostPoints(self, questions: List[List[int]]) -> int:
        self.questions = questions
        return self.my_sol(0)


data = [[3,2],[4,3],[4,4],[2,5]]
r = Solution().mostPoints(data)
print(r)
