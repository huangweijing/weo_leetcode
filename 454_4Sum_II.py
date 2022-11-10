from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        cnt_dict12 = defaultdict(lambda : 0)
        cnt_dict23 = defaultdict(lambda: 0)
        cnt_dict13 = defaultdict(lambda: 0)
        # for i in nums1:
        #     for j in nums2:
        #         cnt_dict12[i + j] += 1
        for i in nums2:
            for j in nums3:
                cnt_dict23[i + j] += 1
        # for i in nums1:
        #     for j in nums3:
        #         cnt_dict13[i + j] += 1
        # for i in nums3:
        #     for j in nums4:
        #         ans += cnt_dict12[-i - j]
        # print(ans)
        for i in nums1:
            for j in nums4:
                ans += cnt_dict23[-i - j]
        # print(ans)
        # for i in nums2:
        #     for j in nums4:
        #         ans += cnt_dict13[-i - j]
        # print(ans)
        return ans

data = [
[0]
,[0]
,[0]
,[0]
]
r = Solution().fourSumCount(* data)
print(r)




