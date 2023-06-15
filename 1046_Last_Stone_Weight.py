from typing import List
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
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = MaximumHeap()
        for stone in stones:
            heap.push(stone)

        while heap.length() > 1:
            s1 = heap.pop()
            s2 = heap.pop()
            if s1 != s2:
                heap.push(abs(s1 - s2))
        return 0 if heap.length() == 0 else heap.top()