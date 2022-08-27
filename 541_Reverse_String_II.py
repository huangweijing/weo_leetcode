class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        for i in range(int(len(s) / k) + 1):
            if i & 1 == 1:
                result += s[i * k: i * k + k]
            else:
                result += s[i * k: i * k + k][::-1]

        return result

r = Solution().reverseStr("abcdefg", 3)
print(r)


