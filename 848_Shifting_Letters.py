from typing import List
from collections import deque


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shi_deq = deque([0])
        for shi in reversed(shifts):
            shi_deq.appendleft(shi + shi_deq[0])
        res = []
        for i, ch in enumerate(s):
            conv = chr(((ord(ch) - ord('a')) + shi_deq[i]) % 26 + ord('a'))
            res.append(conv)
        return "".join(res)


