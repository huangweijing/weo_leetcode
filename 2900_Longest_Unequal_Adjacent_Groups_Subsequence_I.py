from typing import List
from collections import defaultdict

class Solution:

    def getWordsInLongestSubsequence(self, n: int, words: List[str]
                                     , groups: List[int]) -> List[str]:
        dp = [0] * (n + 1)
        dp_words = [list[str]() for _ in range(n + 1)]
        dp[groups[0]] = len(words[0])
        dp_words[groups[0]].append(words[0])
        for i in range(1, n):
            # print("dp", dp)
            new_dp = [0] * (n + 1)
            max_j = -1
            for j in range(n + 1):
                new_dp[j] = max(new_dp[j], dp[j])
                if j != groups[i] and dp[j] + len(words[i]) > new_dp[groups[i]]:
                    # print(dp[j] + len(words[i]), new_dp[groups[i]])
                    new_dp[groups[i]] = dp[j] + len(words[i])
                    # print("new_dp", new_dp)
                    max_j = j
            if max_j != -1:
                dp_words[groups[i]] = dp_words[max_j].copy()
                dp_words[groups[i]].append(words[i])
            dp = new_dp

        # print(dp)
        ans, max_len = [], 0
        for i, val in enumerate(dp):
            if val > max_len:
                max_len = val
                ans = dp_words[i]
        return ans


data = [
    3
    , ["bab","dab","cab"]
    , [1,2,2]
]
r = Solution().getWordsInLongestSubsequence(* data)
print(r)