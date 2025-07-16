from typing import List
import heapq


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        dp = [[[10e9] * 3
               for _ in moveTime[0]]
               for _ in moveTime]
        dp[0][0][1] = 0
        heap = [(0, 0, 0, 1)]
        while len(heap) > 0:
            # print(dp)
            entry = heapq.heappop(heap)
            rIdx, cIdx = entry[1], entry[2]
            cost = entry[3]
            new_cost = 3 - cost
            if rIdx == len(dp) - 1 and cIdx == len(dp[0]) - 1:
                return entry[0]
            if rIdx - 1 >= 0:
                time = max(entry[0], moveTime[rIdx - 1][cIdx]) + cost
                if time < dp[rIdx - 1][cIdx][new_cost]:
                    dp[rIdx - 1][cIdx][new_cost] = time
                    heapq.heappush(heap, (time, rIdx - 1, cIdx, new_cost))
            if cIdx - 1 >= 0:
                time = max(entry[0], moveTime[rIdx][cIdx - 1]) + cost
                if time < dp[rIdx][cIdx - 1][new_cost]:
                    dp[rIdx][cIdx - 1][new_cost] = time
                    heapq.heappush(heap, (time, rIdx, cIdx - 1, new_cost))
            if rIdx + 1 < len(dp):
                time = max(entry[0], moveTime[rIdx + 1][cIdx]) + cost
                if time < dp[rIdx + 1][cIdx][new_cost]:
                    dp[rIdx + 1][cIdx][new_cost] = time
                    heapq.heappush(heap, (time, rIdx + 1, cIdx, new_cost))
            if cIdx + 1 < len(dp[0]):
                time = max(entry[0], moveTime[rIdx][cIdx + 1]) + cost
                if time < dp[rIdx][cIdx + 1][new_cost]:
                    dp[rIdx][cIdx + 1][new_cost] = time
                    heapq.heappush(heap, (time, rIdx, cIdx + 1, new_cost))
            # print(dp, cost)
        return dp[-1][-1]
    

data = [[0,4],[4,4]]
r = Solution().minTimeToReach(data)
print(r)