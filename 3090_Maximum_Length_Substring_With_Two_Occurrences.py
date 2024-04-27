from collections import Counter


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l, r = 0, 0
        cnt = Counter()
        ans = 0
        while l < len(s):
            while r < len(s):
                cnt[s[r]] += 1
                if cnt[s[r]] > 2:
                    r += 1
                    break
                ans = max(ans, r - l + 1)
                r += 1
            while l <= r and l < len(s):
                cnt[s[l]] -= 1
                if cnt[s[l]] == 2:
                    l += 1
                    break
                l += 1
            # print(l, r, ans)
        return ans


r = Solution().maximumLengthSubstring("abcbaaac")
print(r)
