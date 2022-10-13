from collections import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0
        rules = {"type": 0, "color": 1, "name": 2}
        key = rules[ruleKey]
        for item in items:
            if item[key] == ruleValue:
                ans += 1
        return ans

