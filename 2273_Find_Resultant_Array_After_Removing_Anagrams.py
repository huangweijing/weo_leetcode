from typing import List
from collections import Counter


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        last_key = ""
        for word in words:
            cnt = Counter(word)
            key = ""
            for ch in sorted(cnt.keys()):
                key += ch + str(cnt[ch])
            if key != last_key:
                ans.append(word)
            last_key = key
        return ans
