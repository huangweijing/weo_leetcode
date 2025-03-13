from typing import List
import bisect
from collections import Counter


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ans = 0
        ages.sort()
        age_cnt = Counter(ages)
        print(ages)
        for i, age in enumerate(ages):
            age_y = 0.5 * age + 7
            idx_y_left = bisect.bisect_right(ages, age_y)
            idx_y_right = bisect.bisect_left(ages, age) - 1
            # print(f"age={age}, idx_y_left={idx_y_left}, idx_y_right={idx_y_right}, val={max(idx_y_right - idx_y_left + 1, 0) + (age_cnt[age] - 1)}")
            ans += max(idx_y_right - idx_y_left + 1, 0) + (age_cnt[age] - 1 if age > age_y else 0)
        return ans
    

data = [14, 15, 15, 17]
r = Solution().numFriendRequests(data)
print(r)


