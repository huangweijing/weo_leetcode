from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        sum_all = []
        sum_val = 0
        for word in words:
            val = 0
            if word[0] in ('a', 'e', 'i', 'o', 'u') and word[-1] in  ('a', 'e', 'i', 'o', 'u'):
                val = 1
            sum_val += val
            sum_all.append(sum_val)
        ans = []
        for query in queries:
            right = sum_all[query[1]]
            if query[0] == 0:
                left = 0
            else:
                left = sum_all[query[0] - 1]
            ans.append(right - left)
        return ans
