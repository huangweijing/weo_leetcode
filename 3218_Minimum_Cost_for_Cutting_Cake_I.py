from typing import List


class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort()
        verticalCut.sort()
        hc, vc = 1, 1
        ans = 0
        while len(horizontalCut) > 0 or len(verticalCut) > 0:
            hor, ver = 0, 0
            if len(horizontalCut) > 0:
                hor = horizontalCut[-1]
            if len(verticalCut) > 0:
                ver = verticalCut[-1]
            if ver >= hor:
                verticalCut.pop()
                ans += ver * hc
                vc += 1
            else:
                horizontalCut.pop()
                ans += hor * vc
                hc += 1
        return ans
        