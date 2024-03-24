class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        str_set = set[str]()
        for i in range(1, len(s)):
            str_set.add(s[i - 1: i + 1])
        for i in range(1, len(s)):
            if s[i - 1: i + 1][::-1] in str_set:
                return True
        return False
    