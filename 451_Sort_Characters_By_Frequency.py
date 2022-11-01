from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        cnt_list = list(Counter(s).items())
        cnt_list.sort(key=lambda x: x[1], reverse=True)
        ans = ""
        for k, v in cnt_list:
            ans += k * v
        return ans

print(Solution().frequencySort("aaaabbbbbbbccccc"))