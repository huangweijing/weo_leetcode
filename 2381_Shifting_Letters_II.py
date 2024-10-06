from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        step = [0] * (len(s) + 1)
        for shift in shifts:
            step_cnt = 1 if shift[2] == 1 else -1
            step[shift[0]] += step_cnt
            step[shift[1] + 1] -= step_cnt
        ans = ""
        offset = 0
        for i, ch in enumerate(s):
            offset += step[i]
            ans += chr((ord(ch) - ord('a') + (offset % 26) + 26) % 26 + ord('a'))
        return ans
    

data = [
    "abc"
    , [[0,1,0],[1,2,1],[0,2,1]]
]
r = Solution().shiftingLetters(*data)
print(r)