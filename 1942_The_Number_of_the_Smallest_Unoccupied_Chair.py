from typing import List
import heapq


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times = [[time[0], time[1], i] for i, time in enumerate(times)]
        times.sort()
        unoccupied_seats = []
        seated_people = []
        seat_idx = 0
        for i, time in enumerate(times):
            while len(seated_people) > 0 and seated_people[0][0] <= time[0]:
                leaved = heapq.heappop(seated_people)
                heapq.heappush(unoccupied_seats, leaved[1])
            # print(unoccupied_seats)
            if len(unoccupied_seats) > 0:
                seat = heapq.heappop(unoccupied_seats)
                heapq.heappush(seated_people, [time[1], seat])
                if time[2] == targetFriend:
                    return seat
            else:
                heapq.heappush(seated_people, [time[1], seat_idx])
                if time[2] == targetFriend:
                    return seat_idx
                seat_idx += 1
        return -1
    

data = [
    [[1,4],[2,3],[4,6]]
    , 1
]
r = Solution().smallestChair(*data)
print(r)