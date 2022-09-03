from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        task_counter = Counter(tasks)
        most_common = deque(task_counter.most_common(len(task_counter)))
        max_cnt = 0
        max_val = most_common[0][1]
        for task in most_common:
            if task[1] == most_common[0][1]:
                max_cnt += 1

        max_cnt = min(max_cnt, n + 1)
        slots = (n + 1 - max_cnt) * (max_val - 1)
        slots = max(0, slots - (len(tasks) -  max_cnt * max_val))
        return slots + len(tasks)

data_tasks = ["A", "C","C", "C", "C", "E"]
data_n = 2
r = Solution().leastInterval(data_tasks, data_n)
print(r)

# cnt = Counter(data_tasks)

