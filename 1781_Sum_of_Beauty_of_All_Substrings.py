class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        cnt = [[0] * 26 for _ in range(len(s) + 1)]
        for i, ch in enumerate(s):
            cnt[i + 1] = cnt[i].copy()
            cnt[i + 1][ord(ch) - ord("a")] += 1
            for j in range(i):
                entry = [cnt[i + 1][k] - cnt[j][k] for k in range(26)]
                entry
                ans += max(entry) - min(c for c in entry if c > 0)
        # print(cnt)
        return ans
    
r = Solution().beautySum("aabcbaa")
print(r)
