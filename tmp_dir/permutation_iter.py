from collections import deque
from functools import cache

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.ch_lst = characters
        self.co_len = combinationLength
        self.counter = [self.ch_lst[i] for i in range(self.co_len)]
        self.not_used = deque([self.ch_lst[i] for i in range(self.co_len, len(self.ch_lst))])
        self.has_next = True

    def move_next(self):
        while len(self.counter) > 0:
            # print(f"counter={self.counter}, not_used={self.not_used}")
            cur = self.counter.pop()
            bigger_num = -1
            for num in self.not_used:
                if num > cur:
                    bigger_num = num
                    break
            self.not_used.append(cur)
            self.not_used = deque(sorted(self.not_used))
            # print(f"sorted {self.not_used}")
            if bigger_num != -1:
                # print(f"has bigger! counter={self.counter}, not_used={self.not_used}")
                self.not_used.remove(bigger_num)
                self.counter.append(bigger_num)
                while len(self.counter) < self.co_len:
                    self.counter.append(self.not_used.popleft())
                # print(f"has bigger! end: counter={self.counter}, not_used={self.not_used}")
                break
            else:
                # print("no bigger num")
                continue

    def next(self) -> str:
        ans = "".join(self.counter)
        self.move_next()
        return ans

    def hasNext(self) -> bool:
        return self.counter != []

com = CombinationIterator("abcdefghijklmnopq", 15)
for i in range(100000):
    print(com.next())
# print(com.next())
# print(com.next())
# print(com.next())
# print(com.hasNext())
# print(com.next())
# print(com.hasNext())
# print(com.next())
# print(com.hasNext())

# while com.hasNext():
#     print(com.next())
