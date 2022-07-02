from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        last_cut = 0
        max_hor_span = 0
        horizontalCuts.append(h)
        for cut in horizontalCuts:
            span = cut - last_cut
            if span > max_hor_span:
                max_hor_span = span
            last_cut = cut

        last_cut = 0
        max_ver_span = 0
        verticalCuts.append(w)
        for cut in verticalCuts:
            span = cut - last_cut
            if span > max_ver_span:
                max_ver_span = span
            last_cut = cut
        modulo = 10 ** 9 + 7
        return (max_hor_span % modulo) * (max_ver_span % modulo) % modulo

# r = Solution().maxArea(30, 30, [2], [2])
r = Solution().maxArea(1000000000, 1000000000, [2], [2])
# r = Solution().maxArea(5, 4, [3, 1], [1])
print(r)

print(999999996000000004 % (10^9 + 7))
