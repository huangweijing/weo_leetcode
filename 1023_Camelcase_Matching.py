from typing import List

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []
        for query in queries:
            pattern_idx, idx = 0, 0
            matches = True
            while idx < len(query) and pattern_idx < len(pattern):
                if pattern[pattern_idx] == query[idx]:
                    pattern_idx += 1
                    idx += 1
                else:
                    # マッチしない場合、もしチェック対象が大文字で止まっていたらアウト
                    if "A" <= query[idx] <= "Z":
                        matches = False
                        break
                    idx += 1
            # チェック対象の残に大文字が残ってた場合はアウト
            while idx < len(query):
                if "A" <= query[idx] <= "Z":
                    matches = False
                    break
                idx += 1
            # パターンが最後でなかったらアウト
            if pattern_idx != len(pattern):
                matches = False
            ans.append(matches)
        return ans

data = [
    ["uAxaqlzahfialcezsLfj","cAqlzyahaslccezssLfj","AqlezahjarflcezshLfj","AqlzofahaplcejuzsLfj","tAqlzahavslcezsLwzfj","AqlzahalcerrzsLpfonj","AqlzahalceaczdsosLfj","eAqlzbxahalcezelsLfj"]
    , "AqlzahalcezsLfj"
]
r = Solution().camelMatch(* data)
print(r)


