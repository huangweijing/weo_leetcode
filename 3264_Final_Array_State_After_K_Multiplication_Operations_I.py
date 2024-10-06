from typing import List
import heapq


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [[num, i] for i, num in enumerate(nums)]
        heapq.heapify(heap)
        for i in range(k):
            head = heapq.heappop(heap)
            new_head = [head[0] * multiplier, head[1]]
            heapq.heappush(heap, new_head)
        heap.sort(key=lambda x: x[1])
        return [e[0] for e in heap]
