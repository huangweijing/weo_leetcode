import random
from typing import List


class Solution:

    def __init__(self, m: int, n: int):
        self.cnt = m * n - 1
        self.m, self.n = m, n
        self.flipped_set = set[int]()

    def flip(self) -> List[int]:
        val = random.randint(0, self.cnt)
        while val in self.flipped_set:
            val = random.randint(0, self.cnt)
        self.flipped_set.add(val)
        # print(self.flipped_set, val)
        return [val // self.n, val % self.n]

    def reset(self) -> None:
        self.flipped_set.clear()


# print(random.randint(0, 3))

data = [3, 1]
sol = Solution(* data)
for i in range(data[0] * data[1]):
    print(sol.flip())
sol.reset()
for i in range(data[0] * data[1]):
    print(sol.flip())

