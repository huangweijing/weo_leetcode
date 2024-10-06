from collections import Counter


class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        cnt = Counter(s)
        max_cnt = max(cnt.values())
        ch_set = set([ch for ch in cnt if cnt[ch] == max_cnt])
        ans = ""
        for ch in reversed(s):
            if ch in ch_set:
                ans = ch + ans
                ch_set.remove(ch)
        return ans

        