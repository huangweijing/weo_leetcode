class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i = 0
        while i < len(s) - 1 - i:
            if s[: i + 1] == s[-1 - i: ]:
                # found pattern
                # print(s[: i+1])
                forward = 1
                while (i + 1) * (forward + 1) <= len(s) and \
                        s[: i + 1] == s[(i + 1) * forward: (i + 1) * (forward + 1)]:
                    # print(s[(i + 1) * forward: (i + 1) * (forward + 1)])
                    forward += 1
                if (i + 1) * forward == len(s):
                    return True
                elif 2 * ((i + 1) * forward) > len(s) - 1:
                    return False
                else:
                    i = (i + 1) * forward
            else:
                i += 1
        return False

r = Solution().repeatedSubstringPattern("bbbaaaabbbbbbaaaabbbbbbaaaabbb")
print(r)

