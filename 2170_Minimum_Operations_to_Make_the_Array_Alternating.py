from typing import List
from collections import Counter


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        cnt1, cnt2 = Counter(), Counter()
        for i in range(1, len(nums), 2):
            cnt1[nums[i]] += 1
        for i in range(0, len(nums), 2):
            cnt2[nums[i]] += 1
        cnt1_mc, cnt2_mc = cnt1.most_common(2), cnt2.most_common(2)
        # print(cnt1_mc, cnt2_mc)
        if cnt1_mc[0][0] != cnt2_mc[0][0]:
            return len(nums) - cnt1_mc[0][1] - cnt2_mc[0][1]
        else:
            if len(cnt1_mc) == len(cnt2_mc) == 2:
                return len(nums) - max(cnt1_mc[0][1] + cnt2_mc[1][1], cnt1_mc[1][1] + cnt2_mc[0][1])
            elif len(cnt1_mc) == 2:
                return len(nums) - max(cnt1_mc[0][1], cnt1_mc[1][1] + cnt2_mc[0][1])
            elif len(cnt2_mc) == 2:
                return len(nums) - max(cnt2_mc[0][1], cnt2_mc[1][1] + cnt1_mc[0][1])
            else:
                return len(nums) - max(cnt1_mc[0][1], cnt2_mc[0][1])


data = [1]
r = Solution().minimumOperations(data)
print(r)