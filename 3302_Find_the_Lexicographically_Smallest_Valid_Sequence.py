from typing import List
from functools import cache


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        idx1, idx2 = len(word1) - 1, len(word2) - 1
        okay_idx = [len(word1), len(word2)]
        while idx2 >= 0 and idx1 >= 0:
            while idx1 >= idx2 and word1[idx1] != word2[idx2]:
                idx1 -= 1
            # print(word1[idx1], word2[idx2], idx1, idx2)
            if idx1 < idx2 or word1[idx1] != word2[idx2]:
                break
            okay_idx = [idx1, idx2]
            idx2 -= 1
            idx1 -= 1
        ans = []
        # print(okay_idx)
        if okay_idx[1] == 0:
            idx1, idx2 = 0, 0
            chance_used = False
            # ans.append(0)
            while idx2 < len(word2):
                if not chance_used and word1[idx1] != word2[idx2]:
                    chance_used = True
                    ans.append(idx1)
                    idx1 += 1
                    idx2 += 1
                else:
                    while idx1 < len(word1) and word1[idx1] != word2[idx2]:
                        idx1 += 1
                    ans.append(idx1)
                    idx1 += 1
                    idx2 += 1
        else:
            idx1, idx2 = 0, 0
            while idx2 < okay_idx[1] - 1:
                while idx1 < okay_idx[0] - 1 and word1[idx1] != word2[idx2]:
                    idx1 += 1
                if idx1 >= okay_idx[0] - 1 or word1[idx1] != word2[idx2]:
                    return []
                else:
                    ans.append(idx1)
                idx1 += 1
                idx2 += 1
            ans.append(idx1)
            idx1 += 1
            idx2 += 1
            # print(ans)
            while idx2 < len(word2):
                while idx1 < len(word1) and word1[idx1] != word2[idx2]:
                    idx1 += 1
                if idx1 < len(word1) and word1[idx1] == word2[idx2]:
                    ans.append(idx1)
                idx1 += 1
                idx2 += 1
            if len(ans) != len(word2):
                return []
        return ans
    
data = [
    "cbfabdemeffdbab"
    , "deeef"
]
r = Solution().validSequence(*data)
print(r)
