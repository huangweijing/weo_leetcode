import heapq
from functools import cmp_to_key

class ObjectHeap:
    def __init__(self, key=lambda x: x):
        self.data = []
        self.key_func = key
        self.memory = dict[int, object]()

    def top(self):
        if len(self.data) == 0:
            return None
        key = self.data[0]
        return self.memory[key]

    def pop(self) -> object:
        key = heapq.heappop(self.data)
        obj = self.memory[key]
        del self.memory[key]
        return obj

    def push(self, obj: object):
        key = self.key_func(obj)
        self.memory[key] = obj
        heapq.heappush(self.data, key)

    def length(self) -> int:
        return len(self.data)

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