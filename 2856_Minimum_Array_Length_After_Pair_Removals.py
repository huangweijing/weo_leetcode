import heapq
from typing import List
from collections import Counter

class Entry:
    def __init__(self, dig: int, count: int):
        self.dig = dig
        self.count = count

    def __lt__(self, other):
        return self.count > other.count

    def __str__(self):
        return f"{self.dig}, {self.count}"

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        heap = [Entry(dig, count) for dig, count in cnt.items()]
        heapq.heapify(heap)
        key_list = sorted(list(cnt.keys()))
        ans = len(nums)
        finished_set = set[int]()
        for num in key_list:
            if num in finished_set:
                continue
            key_cnt = cnt[num]
            while key_cnt > 0:
                # print(num, list(map(str, heap)), ans)
                if len(heap) == 0:
                    return ans
                entry = heapq.heappop(heap)
                # print("pop", entry.dig, entry.count)
                while len(heap) > 0 and entry.dig <= num:
                    entry = heapq.heappop(heap)
                    # print("pop", entry.dig, entry.count)
                if entry.dig <= num:
                    return ans
                if entry.count > 1:
                    cnt[entry.dig] -= 1
                    ans -= 2
                    entry.count -= 1
                    heapq.heappush(heap, entry)
                    # print("push", entry.dig, entry.count)
                    key_cnt -= 1
                else:
                    finished_set.add(entry.dig)
                    ans -= entry.count * 2
                    key_cnt -= 1
        return ans


data = [1,1,1,1,2,7,7,8,9,10,10,10,10,10]
r = Solution().minLengthAfterRemovals(data)
print(r)