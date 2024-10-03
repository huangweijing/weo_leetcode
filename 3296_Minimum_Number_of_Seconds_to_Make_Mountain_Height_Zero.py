from typing import List
import heapq


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        arr = [[time, time, 1] for time in workerTimes]
        heapq.heapify(arr)
        ans = 0
        while mountainHeight > 0:
            time_info = heapq.heappop(arr)
            ans = max(ans, time_info[0])
            mountainHeight -= 1
            time_info[2] += 1
            time_info[0] += time_info[1] * time_info[2]
            heapq.heappush(arr, time_info)
        return ans