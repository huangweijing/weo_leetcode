class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_len_str = ""
        i = 0
        while i < len(s):
            j = 0
            while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                j = j + 1
            j = j - 1
            sub_str = s[i - j:i + j + 1]
            if len(sub_str) > max_len:
                max_len_str = sub_str
                max_len = len(sub_str)
            j = 0
            while i - j >= 0 and i + 1 + j < len(s) and s[i - j] == s[i + 1 + j]:
                j = j + 1
            if j > 0:
                j = j - 1
                if len(s[i - j:i + j + 2]) > max_len:
                    max_len_str = s[i - j:i + j + 2]
                    max_len = len(s[i - j:i + j + 2])

            i = i + 1
        return max_len_str

sol = Solution()
result = sol.longestPalindrome("abcba2200000022dddddd")

print(result)
# print("3" - "2")
print(int("-+12"))

try:
    pass
except BaseException :
    pass
