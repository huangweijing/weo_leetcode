from typing import List
import heapq


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        heapq.heapify(players)
        heapq.heapify(trainers)
        ans = 0
        while len(players) > 0 and len(trainers) > 0:
            p = heapq.heappop(players)
            while len(trainers) > 0 and p > trainers[0]:
                heapq.heappop(trainers)
            if len(trainers) > 0:
                heapq.heappop(trainers)
                ans += 1
        return ans


data = [
    [1, 1, 1]
    , [10]
]
r = Solution().matchPlayersAndTrainers(* data)
print(r)


