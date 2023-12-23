from typing import List


class Solution:
    def twoEditWords(self, queries: List[str]
                     , dictionary: List[str]) -> List[str]:
        ans = []
        for query in queries:
            found = False
            for word in dictionary:
                err = 0
                for i in range(len(query)):
                    if query[i] != word[i]:
                        err += 1
                        if err > 2:
                            break
                if err <= 2:
                    found = True
                    break
            if found:
                ans.append(query)
        return ans

data = [
    ["word","note","ants","wood"]
    , ["wood","joke","moat"]
]
r = Solution().twoEditWords(*data)
print(r)