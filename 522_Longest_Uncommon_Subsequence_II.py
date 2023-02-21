from typing import List

class Solution:
    def is_subseq(self, str1: str, str2: str):
        idx = 0
        for ch in str1:
            if idx >= len(str2):
                return False
            while ch != str2[idx]:
                idx += 1
                if idx >= len(str2):
                    return False
            idx += 1
        return True

    def findLUSlength(self, strs: List[str]) -> int:
        ans = -1
        for i in range(len(strs)):
            subseq_cnt = 0
            for j in range(len(strs)):
                # if i == j:
                #     continue
                subseq_cnt += 1 if self.is_subseq(strs[i], strs[j]) else 0
                if subseq_cnt > 1:
                    break
            if subseq_cnt == 1:
                ans = max(ans, len(strs[i]))
        return ans

data = ["aaa","aaa","aa"]
r = Solution().findLUSlength(data)
print(r)