from collections import Counter


class Solution:
    VOW_SET = set("aiueo")

    def maxVowels(self, s: str, k: int) -> int:
        cnt = Counter(s[:k])
        vow_cnt = sum([cnt[vow] for vow in Solution.VOW_SET])
        ans = vow_cnt
        for i in range(1, len(s) - k + 1):
            # print(s[i: i + k])
            ch = s[i + k - 1]
            ch_to_remove = s[i - 1]
            if ch in Solution.VOW_SET:
                vow_cnt += 1
            if ch_to_remove in Solution.VOW_SET:
                vow_cnt -= 1
            ans = max(ans, vow_cnt)
        return ans



data = [
    "ibpbhixfiouhdljnjfflpapptrxgcomvnb"
    , 33
]
r = Solution().maxVowels(* data)
print(r)