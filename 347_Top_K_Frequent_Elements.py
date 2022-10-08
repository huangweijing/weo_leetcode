from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        item_list = list(cnt.items())
        item_list.sort(key=lambda x: x[1], reverse=True)
        return [num[0] for num in item_list[:k]]

data_nums = [1,1,1,2,2,3]
data_k = 2
r = Solution().topKFrequent(data_nums, data_k)
print(r)
