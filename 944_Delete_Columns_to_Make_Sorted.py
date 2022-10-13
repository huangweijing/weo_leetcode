from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[j - 1][i] > strs[j][i]:
                    result += 1
                    break
        return result
