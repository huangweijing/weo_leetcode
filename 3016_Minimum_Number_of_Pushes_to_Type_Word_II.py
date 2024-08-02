from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)
        arr = [[k, v] for k, v in cnt.items()]
        arr.sort(key=lambda x: x[1])
        idx = 0
        ans = 0
        while len(arr) > 0:
            entry = arr.pop()
            ans += entry[1] * (idx // 8 + 1)
            idx += 1
        return ans
