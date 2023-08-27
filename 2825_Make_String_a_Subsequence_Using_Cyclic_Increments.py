class Solution:
    def prev_ch(self, ch: str):
        if ch == "a":
            return "z"
        else:
            return chr(ord(ch) - 1)

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        str1_idx = -1
        for idx, ch in enumerate(str2):
            str1_idx += 1
            while str1_idx < len(str1):
                if str1[str1_idx] == ch or str1[str1_idx] == self.prev_ch(ch):
                    break
                str1_idx += 1
            if str1_idx >= len(str1):
                return False
        return True


data = [
    "zc"
    , "ad"
]
r = Solution().canMakeSubsequence(* data)
print(r)
