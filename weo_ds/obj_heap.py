import heapq
from functools import cmp_to_key

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

class Student:
    def __init__(self, age, number):
        self.number = number
        self.age = age

heap = ObjectHeap(key=lambda stu: stu.age * 10000 + stu.number)
heap.push(Student(15, 3282))
heap.push(Student(19, 2282))
heap.push(Student(13, 7282))
heap.push(Student(14, 1182))
while heap.length() > 0:
    print(heap.pop().number)