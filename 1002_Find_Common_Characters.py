from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = Counter(words[0])
        for i in range(1, len(words)):
            cnt = Counter(words[i])
            result_keys = set(result.keys())
            key_inter = set(cnt.keys()).intersection(result_keys)
            # print(key_inter)
            for key in result_keys:
                if key in key_inter:
                    result[key] = min(result[key], cnt[key])
                else:
                    del result[key]

        ans = []
        for key in result:
            if result[key] == 1:
                ans.append(key)
            else:
                ans.extend([key] * result[key])
        return ans

