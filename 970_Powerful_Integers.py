import math
from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound <= 0:
            return []
        ans = set()
        if x == y == 1:
            if 2 <= bound:
                ans.add(2)
        elif x == 1 and y != 1:
            max_j = int(math.log(bound, y)) + 1
            for j in range(max_j):
                num = 1 + y ** j
                if num <= bound:
                    ans.add(num)
        elif x != 1 and y == 1:
            max_i = int(math.log(bound, x)) + 1
            for i in range(max_i):
                num = 1 + x ** i
                if num <= bound:
                    ans.add(num)
        else:
            max_j = int(math.log(bound, y)) + 1
            max_i = int(math.log(bound, x)) + 1
            for i in range(max_i):
                for j in range(max_j):
                    num = x ** i + y ** j
                    if num <= bound:
                        ans.add(num)
        return list(ans)

data = [
    5, 3, 15
]
r = Solution().powerfulIntegers(* data)
r.sort()
print(r)

