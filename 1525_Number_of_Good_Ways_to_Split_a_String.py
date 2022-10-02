from collections import Counter

class Solution:
    def numSplits(self, s: str) -> int:
        rcnt = Counter(s)
        lcnt = Counter()
        result, left, right = 0, 0, len(rcnt)
        for ch in s:
            if lcnt[ch] == 0:
                left += 1
            if rcnt[ch] == 1:
                right -= 1
            lcnt[ch] += 1
            rcnt[ch] -= 1
            if left == right:
                result += 1
        return result

r = Solution().numSplits("asdfsare")
print(r)