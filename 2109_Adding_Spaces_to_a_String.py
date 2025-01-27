from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        idx = 0
        arr = []
        for i, ch in enumerate(s):
            if idx < len(spaces) and i == spaces[idx]:
                arr.append(" ")
                idx += 1
            arr.append(ch)
        return "".join(arr)