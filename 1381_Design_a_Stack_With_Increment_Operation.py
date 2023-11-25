class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.inc_arr = [0] * (maxSize + 1)
        self.stk = []

    def push(self, x: int) -> None:
        if len(self.stk) == self.max_size:
            return
        self.stk.append(x)

    def pop(self) -> int:
        cnt = len(self.stk)
        if cnt == 0:
            return -1
        ret = self.stk.pop() + self.inc_arr[cnt]
        self.inc_arr[cnt - 1] += self.inc_arr[cnt]
        self.inc_arr[cnt] = 0
        return ret

    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self.stk))
        self.inc_arr[k] += val



# Your CustomStack object will be instantiated and called as such:
obj = CustomStack(3)
obj.push(4)
obj.increment(3,2)
obj.push(2)
print(obj.pop())