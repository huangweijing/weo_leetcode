from typing import List
from collections import Counter


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = [0] * 10
        for digit in digits:
            cnt[digit] += 1
        ans = 0
        for n1 in range(0, 10, 2):
            if cnt[n1] > 0:
                cnt[n1] -= 1
                for n2 in range(len(cnt)):
                    # print(n2, cnt)
                    if n2 != 0 and cnt[n2] > 0:
                        cnt[n2] -= 1
                        for n3 in range(len(cnt)):
                            if cnt[n3] > 0:
                                ans += 1
                        cnt[n2] += 1
                cnt[n1] += 1
        return ans
    

data = [1, 2, 3, 4]
r = Solution().totalNumbers(data)
print(r)
