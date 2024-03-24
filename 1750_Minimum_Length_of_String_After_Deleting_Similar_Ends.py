from collections import deque


class Solution:
    def minimumLength(self, s: str) -> int:
        q = deque(s)
        while len(q) > 1:
            if q[0] != q[-1]:
                return len(q)
            else:
                ch = q[0]
                while len(q) > 0 and q[0] == ch:
                    q.popleft()
                while len(q) > 0 and q[-1] == ch:
                    q.pop()
        return len(q)
