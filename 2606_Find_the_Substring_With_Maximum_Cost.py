from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        char_val = dict[str, int]()
        for i, ch in enumerate(chars):
            char_val[ch] = vals[i]
        for i in range(26):
            ch = chr(ord("a") + i)
            if ch not in char_val:
                char_val[ch] = i + 1

        ans, acc = 0, 0
        for ch in s:
            acc += char_val[ch]
            if acc < 0:
                acc = 0
            ans = max(ans, acc)

        return ans
