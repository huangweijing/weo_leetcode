from typing import List
import heapq


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        dp = [[10e9] * len(moveTime[0]) for _ in moveTime]
        dp[0][0] = 0
        heap = [(0, 0, 0)]
        while len(heap) > 0:
            # print(dp)
            entry = heapq.heappop(heap)
            rIdx, cIdx = entry[1], entry[2]
            if rIdx == len(dp) - 1 and cIdx == len(dp[0]) - 1:
                return entry[0]
            if rIdx - 1 >= 0:
                time = max(entry[0] + 1, moveTime[rIdx - 1][cIdx] + 1)
                if time < dp[rIdx - 1][cIdx]:
                    dp[rIdx - 1][cIdx] = time
                    heapq.heappush(heap, (time, rIdx - 1, cIdx))
            if cIdx - 1 >= 0:
                time = max(entry[0] + 1, moveTime[rIdx][cIdx - 1] + 1)
                if time < dp[rIdx][cIdx - 1]:
                    dp[rIdx][cIdx - 1] = time
                    heapq.heappush(heap, (time, rIdx, cIdx - 1))
            if rIdx + 1 < len(dp):
                time = max(entry[0] + 1, moveTime[rIdx + 1][cIdx] + 1)
                if time < dp[rIdx + 1][cIdx]:
                    dp[rIdx + 1][cIdx] = time
                    heapq.heappush(heap, (time, rIdx + 1, cIdx))
            if cIdx + 1 < len(dp[0]):
                time = max(entry[0] + 1, moveTime[rIdx][cIdx + 1] + 1)
                if time < dp[rIdx][cIdx + 1]:
                    dp[rIdx][cIdx + 1] = time
                    heapq.heappush(heap, (time, rIdx, cIdx + 1))
        # print(dp)
        return dp[-1][-1]
    

[[0, 290, 371, 371, 370, 371, 372], 
 [79, 232, 233, 429, 340, 490, 373], 
 [441, 481, 234, 235, 236, 493, 374], 
 [442, 236, 235, 236, 501, 372, 373]]

data = [[275,289,370,277,369,258,85],
        [78 ,231,82 ,428,339,489,214],
        [440,480,166,222,134,492,146],
        [3  ,122,16 ,218,500,166,225]]
r = Solution().minTimeToReach(data)
print(r)
            

        