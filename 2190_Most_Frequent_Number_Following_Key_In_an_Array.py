from typing import List
from collections import Counter


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        cnt = Counter()
        for i, num in enumerate(nums[1:], start=1):
            if key == nums[i - 1]:
                cnt[num] += 1
        return cnt.most_common(1).pop()[0]


data = [
    [1,100,200,1,100]
    , 1]
r = Solution().mostFrequent(* data)
print(r)
