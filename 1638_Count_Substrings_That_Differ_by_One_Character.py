class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        mat = [[0] * len(t) for i in range(len(s))]
        for i in range(len(s)):
            for j in range(len(t)):
                mat[i][j] = (1 if s[i] != t[j] else 0)
        result = 0
        for i in range(len(s)):
            for j in range(len(t)):
                k = 0
                diff = 0
                while i + k < len(s) and j + k < len(t):
                    diff += mat[i + k][j + k]
                    if diff == 1:
                        result += 1
                    elif diff > 1:
                        break
                    k += 1
        return result

data_s = "ab"
data_t = "bb"
r = Solution().countSubstrings(data_s, data_t)
print(r)
