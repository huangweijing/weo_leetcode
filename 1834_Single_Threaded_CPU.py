from typing import List
from collections import deque
import heapq

class ObjectHeap:
    def __init__(self, key=lambda x: x):
        self.data = []
        self.key_func = key
        self.memory = dict[int, list[object]]()
        self.size = 0

    def top(self):
        if len(self.data) == 0:
            return None
        key = self.data[0]
        return self.memory[key][-1]

    def pop(self) -> object:
        key = self.data[0]
        obj = self.memory[key].pop()
        if len(self.memory[key]) == 0:
            del self.memory[key]
            heapq.heappop(self.data)
        self.size -= 1
        return obj

    def push(self, obj: object):
        key = self.key_func(obj)
        if key not in self.memory:
            self.memory[key] = []
            heapq.heappush(self.data, key)
        self.size += 1
        self.memory[key].append(obj)

    def length(self) -> int:
        return self.size

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort(key=lambda x: x[0])
        tasks = deque(tasks)
        pq = ObjectHeap(key=lambda x: x[1] * (10 ** 10) + x[2])
        current_time = tasks[0][0]
        while len(tasks) > 0 and tasks[0][0] <= current_time:
            pq.push(tasks.popleft())

        ans = []
        while pq.length() > 0 or len(tasks) > 0:
            if pq.length() > 0:
                job = pq.pop()
                ans.append(job[2])
                current_time += job[1]
                while len(tasks) > 0 and tasks[0][0] <= current_time:
                    pq.push(tasks.popleft())
            elif len(tasks) > 0:
                current_time = tasks[0][0]
                while len(tasks) > 0 and tasks[0][0] <= current_time:
                    pq.push(tasks.popleft())

        return ans

data = [[7,10],[7,12],[7,5],[7,4],[7,2]]
r = Solution().getOrder(data)
print(r)



