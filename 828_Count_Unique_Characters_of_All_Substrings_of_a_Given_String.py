import bisect

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        ch_cnt = [[0] * 26 for _ in s]
        cur_cnt = [0] * 26
        for i, ch in enumerate(reversed(s)):
            cur_cnt[ord(ch) - ord('A')] += 1
            ch_cnt[-1 - i] = cur_cnt.copy()
        print(ch_cnt)

        for i, ch in enumerate(s):
            pass



Solution().uniqueLetterString("AABB")
