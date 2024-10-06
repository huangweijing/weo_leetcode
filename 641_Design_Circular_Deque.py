class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = [-1] * k
        self.rear_idx = 0
        self.front_idx = 0
        self.cnt = 0

    def insertFront(self, value: int) -> bool:
        if self.cnt == len(self.arr):
            return False
        self.arr[self.front_idx] = value
        if self.cnt == 0:
            self.rear_idx = 1
            self.front_idx = len(self.arr) - 1
        else:
            if self.front_idx == 0:
                self.front_idx = len(self.arr) - 1
            else:
                self.front_idx -= 1
        self.cnt += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.cnt == len(self.arr):
            return False
        self.arr[self.rear_idx] = value
        if self.cnt == 0:
            self.rear_idx = 1
            self.front_idx = len(self.arr) - 1
        else:
            if self.rear_idx == len(self.arr) - 1:
                self.rear_idx = 0
            else:
                self.rear_idx += 1
        self.cnt += 1
        return True

    def deleteFront(self) -> bool:
        if self.cnt == 0:
            return False
        self.cnt -= 1
        if self.front_idx == len(self.arr) - 1:
            self.front_idx = 0
        else:
            self.front_idx += 1
        self.arr[self.front_idx] = -1
        if self.cnt == 0:
            self.rear_idx = 0
            self.front_idx = 0
        return True

    def deleteLast(self) -> bool:
        if self.cnt == 0:
            return False
        self.cnt -= 1
        if self.rear_idx == 0:
            self.rear_idx = len(self.arr) - 1
        else:
            self.rear_idx -= 1
        self.arr[self.rear_idx] = -1
        if self.cnt == 0:
            self.rear_idx = 0
            self.front_idx = 0
        return True

    def getFront(self) -> int:
        if self.front_idx == len(self.arr) - 1:
            return self.arr[0]
        else:
            return self.arr[self.front_idx + 1]

    def getRear(self) -> int:
        if self.rear_idx == 0:
            return self.arr[len(self.arr) - 1]
        else:
            return self.arr[self.rear_idx - 1]

    def isEmpty(self) -> bool:
        return self.cnt == 0

    def isFull(self) -> bool:
        return self.cnt == len(self.arr)


data = [
    ["MyCircularDeque", "insertFront", "getRear", "insertFront", "deleteLast", "getRear", "isFull", "getFront",
     "deleteFront", "isEmpty", "getRear", "getFront", "getFront", "deleteLast", "getRear"]
    , [[30], [332], [], [68], [], [], [], [], [], [], [], [], [], [], []]
]
ssa = MyCircularDeque(*data[1][0])
result = []
for idx, command in enumerate(zip(data[0], data[1])):
    if idx == 0:
        continue
    ret = getattr(ssa, command[0])(* command[1])
    print(command[0], command[1], ret)
    print(ssa.arr, ssa.front_idx, ssa.rear_idx)
    result.append(ret)
print(result)