from typing import List
from collections import deque

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        pushed, popped = deque(pushed), deque(popped)
        try:
            while len(pushed) > 0 or len(popped) > 0:
                # print(stk, pushed, popped)
                if len(stk) != 0 and stk[-1] == popped[0]:
                    stk.pop()
                    popped.popleft()
                else:
                    val = pushed.popleft()
                    stk.append(val)
        except Exception:
            return False
        return True

data = [
    [1,2,3,4,5]
    , [4,3,5,1,2]
]
r = Solution().validateStackSequences(* data)
print(r)