from collections import Counter

class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        ch1, ch2 = pattern[0], pattern[1]
        ch1_cnt, ch2_cnt, ans = 0, 0, 0
        for ch in text:
            if ch == ch2:
                ch2_cnt += 1
                ans += ch1_cnt
            if ch == ch1:
                ch1_cnt += 1
        return max(ch1_cnt, ch2_cnt) + ans

r = Solution().maximumSubsequenceCount("fwymvreuftzgrcrxczjacqovduqaiig", "yy")
print(r)