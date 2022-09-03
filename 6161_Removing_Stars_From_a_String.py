from collections import deque

class Solution:
    def removeStars(self, s: str) -> str:
        s = deque(s)
        result = list[str]()
        while len(s) > 0:
            ch = s.popleft()
            if ch == "*":
                if len(result) > 0:
                    result.pop()
            else:
                result.append(ch)
        return "".join(result)

