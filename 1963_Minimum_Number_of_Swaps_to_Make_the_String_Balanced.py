import math


class Solution:
    def minSwaps(self, s: str) -> int:
        stk = []
        for ch in s:
            if ch == "[":
                stk.append(ch)
            elif ch == "]":
                if len(stk) > 0 and stk[-1] == "[":
                    stk.pop()
                else:
                    stk.append("]")
        return math.ceil(len(stk) / 4)
