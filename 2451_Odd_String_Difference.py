from typing import List
from collections import Counter

class Solution:
    def oddString(self, words: List[str]) -> str:
        res_cnt = Counter()
        res_dict = dict[str, str]()
        for word in words:
            key_str = ""
            for i in range(1, len(word)):
                key_str += str(ord(word[i]) - ord(word[i - 1])) + "."
            res_cnt[key_str] += 1
            res_dict[key_str] = word
        # print(res_dict, res_cnt)
        for key, val in res_cnt.items():
            if val == 1:
                return res_dict[key]
        return ""

r = Solution().oddString(["abm","bcn","alm"])
print(r)