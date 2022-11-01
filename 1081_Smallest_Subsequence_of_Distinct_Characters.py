from collections import Counter, defaultdict, deque

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        ans = []
        last_idx = dict[str, int]()

        for i, ch in enumerate(s):
            last_idx[ch] = i

        for i, ch in enumerate(s):
            if ch in ans:
                continue
            while len(ans) > 0 and ch < ans[-1] and i < last_idx[ans[-1]]:
                ans.pop()
            ans.append(ch)

        return "".join(ans)

r = Solution().smallestSubsequence("cbaacabcaaccaacababa")
print(r)
