from collections import deque

class MyStack:

    def __init__(self):
        self.data_queue = deque()

    def push(self, x: int) -> None:
        self.data_queue.append(x)

    def pop(self) -> int:
        tmp_queue = deque()
        while len(self.data_queue) > 1:
            tmp_queue.append(self.data_queue.popleft())
        ret = self.data_queue.popleft()
        self.data_queue = tmp_queue
        return ret

    def top(self) -> int:
        tmp_queue = deque()
        while len(self.data_queue) > 1:
            tmp_queue.append(self.data_queue.popleft())
        ret = self.data_queue.popleft()
        tmp_queue.append(ret)
        self.data_queue = tmp_queue
        return ret

    def empty(self) -> bool:
        return len(self.data_queue) == 0