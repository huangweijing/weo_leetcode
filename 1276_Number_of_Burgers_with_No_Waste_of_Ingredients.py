from typing import List

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices > cheeseSlices * 4 or tomatoSlices < cheeseSlices * 2 \
                or tomatoSlices & 1 == 1:
            return []
        jumbo = (tomatoSlices - cheeseSlices * 2) >> 1
        return [jumbo, cheeseSlices - jumbo]


data = [
    2537427
    , 860448
]
r = Solution().numOfBurgers(* data)
print(r)