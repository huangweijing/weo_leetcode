from collections import deque
from functools import cache

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.ch_lst = characters
        self.co_len = combinationLength
        self.ans = self.generate(deque(self.ch_lst), self.co_len)
        # print(self.ans)
        self.index = 0

    def generate(self, ch_lis: deque, length: int) -> list[str]:
        # print(f"generate: {ch_lis}, {length}")
        if length == 1:
            return list(ch_lis.copy())
        ans = []
        while len(ch_lis) >= length:
            ch = ch_lis.popleft()
            sub_sol = self.generate(ch_lis.copy(), length - 1)
            for sub in sub_sol:
                ans.append(ch + sub)
        return ans

    def next(self) -> str:
        val = self.ans[self.index]
        self.index += 1
        return val

    def hasNext(self) -> bool:
        return self.index < len(self.ans)

com = CombinationIterator("fiklnuy", 3)
while com.hasNext():
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
