from typing import List
from collections import defaultdict, Counter


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        players = defaultdict(lambda: Counter())
        for p in pick:
            players[p[0]][p[1]] += 1
        # print(players)
        ans = 0
        for p, res in players.items():
            # print(res.most_common())
            if res.most_common()[0][1] > p:
                ans += 1
        return ans


data = [
    4
    , [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]
]
r = Solution().winningPlayerCount(*data)
print(r)