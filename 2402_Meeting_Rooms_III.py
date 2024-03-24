from typing import List
import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        # print(meetings)
        room_heap = []
        ready_heap = []
        for i in range(n):
            ready_heap.append([i, 0])
        heapq.heapify(ready_heap)
        room_cnt = [0] * n
        for m in meetings:
            while len(room_heap) > 0 and m[0] >= room_heap[0][0]:
                room = heapq.heappop(room_heap)
                heapq.heappush(ready_heap, [room[1], room[0]])
            # print(ready_heap)
            # print(room_heap)
            # print("-------")
            if len(ready_heap) > 0:
                room = heapq.heappop(ready_heap)
                room_cnt[room[0]] += 1
                heapq.heappush(room_heap, [m[1], room[0]])
            else:
                room = heapq.heappop(room_heap)
                room[0] = room[0] + m[1] - m[0]
                heapq.heappush(room_heap, room)
                room_cnt[room[1]] += 1
        max_room_cnt = 0
        ans = -1
        for i, cnt in enumerate(room_cnt):
            if cnt > max_room_cnt:
                max_room_cnt = cnt
                ans = i
        return ans

data = [
    3
    , [[1,20],[2,10],[3,5],[4,9],[6,8]]
]
r = Solution().mostBooked(*data)
print(r)


