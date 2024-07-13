from typing import List


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        str_set = set(s)
        for i in range(ord('a'), ord('z') + 1):
            if chr(i) in str_set and chr(i).upper() not in str_set:
                pass
        return ""


