class Solution:
    def reverseString(self, s: List[str]) -> None:
        mid = len(s) >> 1
        for i in range(mid):
            tmp = s[-1 - i]
            s[-1 - i] = s[i]
            s[i] = tmp
