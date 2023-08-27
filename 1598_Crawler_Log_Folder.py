from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []
        for log in logs:
            if log == "../":
                if len(stk) > 0:
                    stk.pop()
            elif log == "./":
                pass
            else:
                stk.append(log)
        return len(stk)