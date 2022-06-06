class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i, ch in enumerate(haystack):
            found_u = False
            match_cnt = 0
            for j in range(len(needle)):
                if i + j < len(haystack) and haystack[i + j] == needle[j]:
                    match_cnt += 1
                else:
                    break
            if match_cnt == len(needle):
                return i
        return -1

s = Solution()
r = s.strStr("mississippi", "issip")
print(r)