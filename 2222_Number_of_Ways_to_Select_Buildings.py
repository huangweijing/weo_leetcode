from collections import Counter


class Solution:
    def numberOfWays(self, s: str) -> int:
        cnt_after = Counter(s)
        cnt_before = Counter()
        ans = 0
        for i, ch in enumerate(s):
            cnt_after[s[i]] -= 1
            if i - 1 >= 0:
                cnt_before[s[i - 1]] += 1
            if ch == "0":
                ans += cnt_after["1"] * cnt_before["1"]
            else:
                ans += cnt_after["0"] * cnt_before["0"]
        return ans





