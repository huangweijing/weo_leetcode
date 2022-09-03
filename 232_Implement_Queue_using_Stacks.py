class MyQueue:

    def __init__(self):
        self.data_stack = list[int]()

    def push(self, x: int) -> None:
        self.data_stack.append(x)

    def pop(self) -> int:
        tmp_stack = list[int]()
        while len(self.data_stack) > 1:
            tmp_stack.append(self.data_stack.pop())
        ret = self.data_stack.pop()
        while len(tmp_stack) > 0:
            self.data_stack.append(tmp_stack.pop())
        return ret

    def peek(self) -> int:
        tmp_stack = list[int]()
        while len(self.data_stack) > 1:
            tmp_stack.append(self.data_stack.pop())
        ret = self.data_stack.pop()
        tmp_stack.append(ret)
        while len(tmp_stack) > 0:
            self.data_stack.append(tmp_stack.pop())
        return ret

    def empty(self) -> bool:
        return len(self.data_stack) == 0
