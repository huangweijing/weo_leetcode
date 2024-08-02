import heapq
from collections import deque

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        q = deque(s)
        heap = []
        for _ in range(k):
            heap.append(q.popleft())
        heapq.heapify(heap)
        while True:
            ch = heapq.heappop(heap)
            
