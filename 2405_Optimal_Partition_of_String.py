from collections import Counter

class Solution:
    def partitionString(self, s: str) -> int:
        ch_set = set[str]()
        ans = 0
        for ch in s:
            if ch in ch_set:
                ch_set = set[str]()
                ans += 1
            ch_set.add(ch)
        if len(ch_set) > 0:
            ans += 1
        return ans
