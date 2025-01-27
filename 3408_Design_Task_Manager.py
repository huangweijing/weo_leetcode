from typing import List
from collections import Counter
import heapq

class Task:
    def __init__(self, userId: int, taskId: int, priority: int, version: int) -> None:
        self.user_id = userId
        self.task_id = taskId
        self.priority = priority
        self.version = version
    
    def __lt__(self, obj) -> bool:
        if self.priority > obj.priority:
            return True
        elif self.priority == obj.priority:
            if self.task_id > obj.task_id:
                return True
        return False
    
    def __str__(self) -> str:
        return f"key=<{self.task_id},{self.version}>,priority={self.priority},user_id={self.user_id}"


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_priority_dict = dict[tuple[int, int], Task]()
        self.task_id_map = Counter()
        self.task_heap = []
        for t in tasks:
            task = Task(t[0], t[1], t[2], self.task_id_map[t[1]])
            key = (task.task_id, task.version)
            self.task_priority_dict[key] = task
            heapq.heappush(self.task_heap, task)
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        task = Task(userId=userId, taskId=taskId
                    , priority=priority, version=self.task_id_map[taskId])
        key = (task.task_id, task.version)
        self.task_priority_dict[key] = task
        heapq.heappush(self.task_heap, task)
        

    def edit(self, taskId: int, newPriority: int) -> None:
        key = (taskId, self.task_id_map[taskId])
        # if key in self.task_priority_dict:
        task = self.task_priority_dict[key]
        del self.task_priority_dict[key]
        self.task_id_map[taskId] += 1
        task = Task(task.user_id, task.task_id, newPriority, self.task_id_map[taskId])
        heapq.heappush(self.task_heap, task)
        self.task_priority_dict[(task.task_id, task.version)] = task


    def rmv(self, taskId: int) -> None:
        key = (taskId, self.task_id_map[taskId])
        if key in self.task_priority_dict:
            del self.task_priority_dict[key]
        self.task_id_map[taskId] += 1
        

    def execTop(self) -> int:
        while len(self.task_heap) > 0:
            task = heapq.heappop(self.task_heap)
            if self.task_id_map[task.task_id] != task.version:
                continue
            # heapq.heappush(self.task_heap, task)
            return task.user_id         
        return -1   



data = [
    ["TaskManager","edit","edit","execTop"]
    , [[[[2,18,1],[10,5,12],[5,11,39],[7,12,22],[6,9,24],[7,2,49],[1,8,3]]],[8,21],[8,11],[]]
]
ssa = TaskManager(*data[1][0])
result = []
for idx, command in enumerate(zip(data[0], data[1])):
    if idx == 0:
        continue
    ret = getattr(ssa, command[0])(* command[1])
    print(command[0], command[1], ret)
    print([str(v) for v in ssa.task_heap])
    print("-----")
    result.append(ret)
print(result)