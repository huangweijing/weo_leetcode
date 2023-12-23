from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        cnt = Counter(s)
        tar_cnt = Counter(target)
        ans = len(s)
        for ch, c in tar_cnt.items():
            ans = min(ans, cnt[ch] // c)
        return ans
