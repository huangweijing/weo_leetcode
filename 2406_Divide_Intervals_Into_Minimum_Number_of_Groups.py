from typing import List
import heapq


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if len(heap) > 0 and heap[0] < interval[0]:
                    heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
        return len(heap)


