import heapq


class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stk = []
        self.inc_stk = []
        

    def push(self, x: int) -> None:
        if len(self.stk) < self.maxSize:
            self.stk.append(x)
        
    def pop(self) -> int:
        if len(self.stk) == 0:
            return -1
        plus = 0
        while len(self.inc_stk) > 0 and -(self.inc_stk[0][0]) >= len(self.stk):
            inc = heapq.heappop(self.inc_stk)[1]
            plus += inc
        ret = self.stk.pop() + plus
        if len(self.stk) > 0 and plus > 0:
            self.increment(len(self.stk), plus)
        return ret
        
    def increment(self, k: int, val: int) -> None:
        k = min(len(self.stk), k)
        heapq.heappush(self.inc_stk, [-k, val])
        


# Your CustomStack object will be instantiated and called as such:
data = [
    ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
    , [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
]
ssa = CustomStack(*data[1][0])
result = []
for idx, command in enumerate(zip(data[0], data[1])):
    if idx == 0:
        continue
    ret = getattr(ssa, command[0])(* command[1])
    print(command[0], command[1], ret)
    print(ssa.stk)
    print(ssa.inc_stk)
    print("-------")
    result.append(ret)
print(result)