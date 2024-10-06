from typing import List
import heapq
from collections import deque


class Worker:
    def __init__(self, cost: int, idx: int) -> None:
        self.cost = cost
        self.idx = idx
        self.pick_from = ""

    def __lt__(self, other) -> bool:
        if self.cost < other.cost:
            return True
        elif self.cost > other.cost:
            return False
        else:
            return self.idx < other.idx


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        worker_queue = deque([Worker(cost, i) for i, cost in enumerate(costs)])
        heap = []
        ans = 0
        for _ in range(candidates):
            if len(worker_queue) == 0:
                break
            worker = worker_queue.popleft()
            worker.pick_from = "left"
            heapq.heappush(heap, worker)
        for _ in range(candidates):
            if len(worker_queue) == 0:
                break
            worker = worker_queue.pop()
            worker.pick_from = "right"
            heapq.heappush(heap, worker)
        while k > 0:
            worker = heapq.heappop(heap)
            ans += worker.cost
            if len(worker_queue) > 0:
                if worker.pick_from == "left":
                    new_worker = worker_queue.popleft()
                    new_worker.pick_from = "left"
                    heapq.heappush(heap, new_worker)
                else:
                    new_worker = worker_queue.pop()
                    new_worker.pick_from = "right"
                    heapq.heappush(heap, new_worker)
            k -= 1
        return ans


data = [
    [31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58]
    , 11
    , 2
]
r = Solution().totalCost(*data)
print(r)