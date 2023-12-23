from typing import List
from collections import Counter


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        ans = [0, 0, 0, 0, 0]
        for i, c in enumerate(count):
            if c != 0:
                ans[0] = i
                break
        for i, c in enumerate(reversed(count)):
            if c != 0:
                ans[1] = len(count) - 1 - i
                break
        cnt_all = sum(c for c in count)
        sum_all = sum(i * c for i, c in enumerate(count))
        ans[2] = sum_all / cnt_all
        visited = 0
        if cnt_all & 1 == 1:
            for i, c in enumerate(count):
                if visited + c >= (cnt_all >> 1) + 1:
                    ans[3] = i
                    break
                visited += c
        else:
            found = 0
            for i, c in enumerate(count):
                c_val = c
                if found == 0 and visited + c >= cnt_all >> 1:
                    ans[3] += i
                    found += 1
                    c_val -= 1
                if found == 1 and c_val > 0 and visited + c >= (cnt_all >> 1) + 1:
                    ans[3] += i
                    found += 1
                visited += c
                if found == 2:
                    break
            ans[3] /= 2
        freq = 0
        for i, c in enumerate(count):
            if c > freq:
                ans[4] = i
                freq = c
        return ans

data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
r = Solution().sampleStats(data)
print(r)

