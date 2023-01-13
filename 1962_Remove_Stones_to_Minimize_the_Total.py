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
    def minStoneSum(self, piles: List[int], k: int) -> int:
        hq = MaximumHeap()
        for pile in piles:
            hq.push(pile)
        while k > 0:
            pile = hq.pop()
            pile -= pile // 2
            hq.push(pile)
            k -= 1
        return -sum(hq.data)
