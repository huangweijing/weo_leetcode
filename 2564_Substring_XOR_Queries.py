from typing import List


class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        pos = dict[str, int]()
        for i in range(1, min(31, len(s) + 1)):
            for j in range(i, len(s) + 1):
                key = s[j - i: j]
                if key not in pos:
                    pos[key] = j - i
        ans = []
        for query in queries:
            val = bin(query[0] ^ query[1])[2:]
            if val in pos:
                idx = pos[val]
                ans.append([idx, idx + len(val) - 1])
            else:
                ans.append([-1, -1])
        return ans
    
data = [
    "1"
    , [[4,5]]
]
r = Solution().substringXorQueries(*data)
print(r)