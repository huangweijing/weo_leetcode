from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = 0
        for ant_pos in left:
            ans = max(ans, ant_pos + 1)
        for ant_pos in right:
            ans = max(ans, n - ant_pos + 1)
        return ans
