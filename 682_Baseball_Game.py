from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for op in operations:
            if op == "C":
                stk.pop()
            elif op == "D":
                stk.append(stk[-1] * 2)
            elif op == "+":
                stk.append(stk[-1] + stk[-2])
            else:
                stk.append(int(op))
        return sum(stk)
