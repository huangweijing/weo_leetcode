from collections import Counter


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        last_pat_idx = -1
        ans = 0
        while last_pat_idx < len(s):
            cnt = Counter()
            new_idx = -1
            for i in range(last_pat_idx, len(s)):
                cnt[s[i]] += 1
                if len(set(cnt.values())) == 1:
                    new_idx = last_pat_idx
                    ans += 1
            last_pat_idx = new_idx
        return ans
    

r = Solution().minimumSubstringsInPartition("fabccddg")
print(r)