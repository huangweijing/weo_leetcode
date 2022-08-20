class Solution:
    def firstUniqChar(self, s: str) -> int:
        ch_cnt = dict[str, int]()
        for ch in s:
            if ch not in ch_cnt:
                ch_cnt[ch] = 0
            ch_cnt[ch] += 1

        for i, ch in enumerate(s):
            if ch_cnt[ch] == 1:
                return i
        return -1