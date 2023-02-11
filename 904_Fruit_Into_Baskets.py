from typing import List
from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        left, right = 0, 0
        cnt = Counter()
        while left < len(fruits):
            while right < len(fruits) and (fruits[right] in cnt or len(cnt) < 2):
                cnt[fruits[right]] += 1
                right += 1
            # print(cnt)
            ans = max(ans, sum([v for k, v in cnt.items()]))
            cnt[fruits[left]] -= 1
            if cnt[fruits[left]] == 0:
                del cnt[fruits[left]]
            left += 1
        return ans

r = Solution().totalFruit([1,2,3,2,2])
print(r)



