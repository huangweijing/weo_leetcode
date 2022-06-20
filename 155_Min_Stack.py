class MinStack:

    def __init__(self):
        self.my_stack = list()
        self.min_stack = list()

    def push(self, val: int) -> None:
        self.my_stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            last_min = self.min_stack[-1]
            self.min_stack.append(last_min if last_min < val else val)

    def pop(self) -> None:
        self.my_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.my_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()