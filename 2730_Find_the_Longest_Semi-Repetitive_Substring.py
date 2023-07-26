from collections import Counter, deque

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        old_ch = ""
        rep_arr = deque()
        for i, ch in enumerate(s):
            if ch == old_ch:
                rep_arr.append(i)
            old_ch = ch
        rep_arr.appendleft(-1)
        rep_arr.append(len(s) + 1)
        # print(rep_arr)
        if len(rep_arr) <= 3:
            return len(s)
        ans = -1
        for i, idx in enumerate(list(rep_arr)[2:], start=2):
            start = rep_arr[i - 2]
            end = idx - 1
            if start < 0:
                start = 0
            if end >= len(s):
                end = len(s) - 1
            # print(start, end)
            ans = max(ans, end - start + 1)
        return ans


data = "24489929009"
data = "52233"
r = Solution().longestSemiRepetitiveSubstring(data)
print(r)

