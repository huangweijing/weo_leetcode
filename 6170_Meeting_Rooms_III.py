import heapq
from typing import List

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
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
