from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_dict = { e[0]: e[1] for e in knowledge }
        ans = ""
        idx = 0
        while idx < len(s):
            while s[idx] == "(":
                idx += 1
                key_start = idx
                while s[idx] != ")":
                    idx += 1
                key = s[key_start: idx]
                if key in knowledge_dict:
                    ans += knowledge_dict[key]
                else:
                    ans += "?"
                idx += 1
                if idx >= len(s):
                    return ans
            ans += s[idx]
            idx += 1
        return ans

data = [
    "(name)(age)yearsold"
    , [["name","bob"],["age2","two"]]
]
r = Solution().evaluate(* data)
print(r)