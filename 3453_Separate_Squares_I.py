from typing import List


class Solution:
    def __init__(self) -> None:
        self.sqr = []
        self.total_size = 0

    def my_sol(self, line: float) -> bool:
        up_size = 0
        for s in self.sqr:
            up_size += s[2] * min(s[2], max(s[1] + s[2] - line, 0))
            if up_size > self.total_size - up_size: 
                return True
        return False

    def separateSquares(self, squares: List[List[int]]) -> float:
        self.sqr = squares
        self.total_size = sum([s[2] ** 2 for s in squares])
        down = min([s[1] for s in squares])
        up = max(s[1] + s[2] for s in squares)
        mid = (down + up) / 2
        while True:
            r1 = self.my_sol(mid)
            r2 = self.my_sol(mid - 0.00001)
            if not r1 and r2:
                return mid
            elif r1 and r2:
                down = mid
            elif not r1 and not r2:
                up = mid
            mid = (down + up) / 2


data = [[0,0,1],[2,2,1]]
sol = Solution()
r = sol.separateSquares(data)
print(r)