class MyCircularQueue:

    def __init__(self, k: int):
        self.storage = [-1] * k
        self.head_idx = 0
        self.rear_idx = -1
        self.size = 0
        self.max_size = k

    def enQueue(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        if self.rear_idx == self.max_size - 1:
            self.rear_idx = 0
        else:
            self.rear_idx += 1
        self.storage[self.rear_idx] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.storage[self.head_idx] = -1
        if self.head_idx == self.max_size - 1:
            self.head_idx = 0
        else:
            self.head_idx += 1
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.storage[self.head_idx]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.storage[self.rear_idx]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size

data = [["MyCircularQueue","enQueue","Rear","Rear","deQueue","enQueue","Rear","deQueue","Front","deQueue","deQueue","deQueue"]
        ,[[6],[6],[],[],[],[5],[],[],[],[],[],[]]]
q = MyCircularQueue(*data[1][0])
for i in range(1, len(data[0][1:])):
    func = getattr(q, data[0][i])
    r = func(*data[1][i])
    print(f"func={data[0][i]}, args={data[1][i]}, return={r}")
    print(q.storage, q.head_idx, q.rear_idx)


# print(q.enQueue(3))
# print(q.enQueue(4))
# print(q.enQueue(5))
# print(q.Front())
# print(q.Rear())
# print(q.deQueue())
# print(q.Rear())