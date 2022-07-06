class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        str_list = list(columnTitle)
        str_list.reverse()
        exp = 0
        result = 0
        for ch in str_list:
            result += (26 ** exp) * (ord(ch) - ord("A") + 1)
            exp += 1
        return result

r = Solution().titleToNumber("AA")
print(r)