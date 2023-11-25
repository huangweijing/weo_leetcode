from collections import defaultdict, Counter

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        start_ch, end_ch = set[str](), set[str]()
        tmp_dict = defaultdict(lambda :Counter())
        val_dict = defaultdict(lambda :Counter())
        for ch in s:
            new_added = ""
            if ch not in start_ch:
                start_ch.add(ch)
                new_added = ch
            else:
                for k, v in tmp_dict[ch].items():
                    val_dict[ch][k] += v
                    tmp_dict[ch][k] -= v
            for sc in start_ch:
                if new_added != sc:
                    tmp_dict[sc][ch] += 1
        ans = 0
        for cnt in val_dict.values():
            ans += len(cnt)
        return ans


data = "bbcbaba"
r = Solution().countPalindromicSubsequence(data)
print(r)