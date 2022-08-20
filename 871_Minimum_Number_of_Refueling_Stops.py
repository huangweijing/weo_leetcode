from typing import List
from collections import deque
import heapq

class MaximumHeap:
    def __init__(self):
        self.data = []
        heapq.heapify(self.data)

    def top(self):
        if len(self.data) == 0:
            return None
        return -self.data[0]

    def pop(self) -> int:
        return -heapq.heappop(self.data)

    def push(self, num: int):
        heapq.heappush(self.data, -num)

    def length(self) -> int:
        return len(self.data)

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.sort(key=lambda k: k[0])
        stations = deque(stations)

        best_station_rank = MaximumHeap()
        distance = startFuel
        station_cnt = 0
        while distance < target:
            # print(distance, target, stations)
            while len(stations) > 0 and stations[0][0] <= distance:
                sta = stations.popleft()
                best_station_rank.push(sta[1])
            if best_station_rank.length() > 0:
                best_sta = best_station_rank.pop()
                distance += best_sta
                station_cnt += 1
            else:
                return -1
        return station_cnt


target = 100
startFuel = 50
stations = [[25, 25], [50, 50]]

r = Solution().minRefuelStops(target, startFuel, stations)
print(r)



