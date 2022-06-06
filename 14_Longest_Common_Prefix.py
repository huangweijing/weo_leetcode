class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        first_str = strs[0]
        for i in range(len(first_str)):
            for s in strs:
                if len(s) <= i:
                    return result
                if s[i] != first_str[i]:
                    return result
            result = result + first_str[i]
        return result




sol = Solution()
result = sol.longestCommonPrefix(["flower", "flow", "flight"])
print(result)