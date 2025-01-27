from collections import defaultdict


class Solution:
    def __init__(self) -> None:
        self.len_arr = []

    def maximumLength(self, s: str) -> int:
        last = ""
        len_arr = [0] * len(s)
        for i, ch in enumerate(reversed(s)):
            idx = len(s) - 1 - i
            if ch == last:
                len_arr[idx] = len_arr[idx + 1] + 1
            else:
                len_arr[idx] = 1
            last = ch
        cnt = defaultdict(lambda: list[int]())
        for i, ch in enumerate(s):
            cnt[ch].append(len_arr[i])
        ans = -1
        for key in cnt:
            if len(cnt[key]) >= 3:
                cnt[key].sort(reverse=True)
                ans = max(ans, cnt[key][2])
        return ans
    

data = "abcaba"
r = Solution().maximumLength(data)
print(r)

