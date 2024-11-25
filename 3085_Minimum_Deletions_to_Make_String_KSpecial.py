from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)
        ans = 1e9
        for i in range (max(cnt.values()) + 1):
            cost = 0
            for key in cnt:
                if i - k <= cnt[key] <= i:
                    continue
                elif cnt[key] < i - k:
                    cost += cnt[key]
                elif cnt[key] > i:
                    cost += cnt[key] - i
            # print(i, cost)
            ans = min(ans, cost)
        return ans
    
data = [
    "dabdcbdcdcd"
    , 2
]
r = Solution().minimumDeletions(*data)
print(r)