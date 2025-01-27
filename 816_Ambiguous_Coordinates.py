from typing import List


class Solution:
    def add_dot(self, s: str) -> list[str]:
        ret = list[int]()
        if len(s) > 1 and s == "0" * len(s):
            return ret
        if not (len(s) > 1 and s[0] == "0"):
            ret.append(s)
        for i in range(1, len(s)):
            if s[:i] == "00":
                break
            if s[-1] == "0":
                break
            if len(s[:i]) > 1 and s[0] == "0":
                break
            ret.append(s[:i] + "." + s[i:])
        return ret

    def ambiguousCoordinates(self, s: str) -> List[str]:
        ans = set[str]()
        num = s[1:-1]
        for i in range(1, len(num)):
            lst1 = self.add_dot(num[:i])
            lst2 = self.add_dot(num[i:])
            # print(lst1, lst2)
            for word1 in lst1:
                for word2 in lst2:
                    ans.add(f"({word1}, {word2})")
        return list(ans)
    

data = "(100)"
r = Solution().ambiguousCoordinates(data)
print(r)