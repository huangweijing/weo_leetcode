from typing import List

class Solution:
    def __init__(self):
        self.time = []
        self.total_trips = 0

    def count_trip(self, total_time) -> int:
        trip_cnt = 0
        for time in self.time:
            trip_cnt += total_time // time
        return trip_cnt

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        left, right = 0, time[0] * totalTrips + 1
        mid = left + right >> 1
        self.time = time
        self.total_trips = totalTrips
        # print(self.count_trip(9))
        while left <= right:
            mid = left + right >> 1
            # print(left, mid, right)
            trip_cnt = self.count_trip(mid)
            if trip_cnt >= totalTrips:
                if self.count_trip(mid - 1) < totalTrips:
                    return mid
                else:
                    right = mid - 1
            elif trip_cnt < totalTrips:
                left = mid + 1
        return mid


data = [
    [3,3,8]
    , 6
]
r = Solution().minimumTime(* data)
print(r)