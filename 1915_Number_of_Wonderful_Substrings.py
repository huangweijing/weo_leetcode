from collections import Counter


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cnt = Counter()
        cnt[0] += 1
        status = 0
        ans = 0
        for ch in word:
            status ^= 1 << (ord(ch) - ord("a"))
            ans += cnt[status]
            # print(bin(status))
            for i in range(ord("a"), ord("j") + 1):
                new_status = status ^ (1 << (i - ord("a")))
                # print(bin(new_status), cnt[new_status])
                ans += cnt[new_status]
            cnt[status] += 1
        # print(cnt)
        return ans


word = "aabb"
r = Solution().wonderfulSubstrings(word)
print(r)