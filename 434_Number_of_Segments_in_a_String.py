class Solution:
    def countSegments(self, s: str) -> int:
        s = s.strip()
        s_arr = s.split(sep=" ")
        result = 0
        for sub in s_arr:
            if len(sub.strip()) > 0:
                result += 1

        return result
