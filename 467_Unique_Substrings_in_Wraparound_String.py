class Solution:
    def is_next(self, ch1: str, ch2: str) -> bool:
        if ord(ch2) - ord(ch1) == 1:
            return True
        if ch1 == "z" and ch2 == "a":
            return True
        return False

    def findSubstringInWraproundString(self, s: str) -> int:
        idx = 0
        max_str_len = 0
        max_arr = [0] * 26
        while idx < len(s):
            if idx == 0 or not self.is_next(s[idx - 1], s[idx]):
                max_str_len = 1
            else:
                max_str_len += 1
            max_arr[ord(s[idx]) - ord("a")] = max(max_str_len, max_arr[ord(s[idx]) - ord("a")])
            idx += 1
        
        return sum(max_arr)
        