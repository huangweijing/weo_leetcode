from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = 0
        for s in sentences:
            result = max(result, s.count(" ") + 1)
        return result