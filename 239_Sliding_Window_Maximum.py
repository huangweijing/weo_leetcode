from collections import deque
import heapq
from typing import List

class MaximumHeap:
    def __init__(self):
        self.data = []
        heapq.heapify(self.data)

    def top(self):
        if len(self.data) == 0:
            return None
        return -self.data[0]

    def pop(self) -> int:
        return -heapq.heappop(self.data)

    def push(self, num: int):
        heapq.heappush(self.data, -num)

    def length(self) -> int:
        return len(self.data)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = MaximumHeap()
        val_hash = dict[int, deque]()
        result = []
        for i, num in enumerate(nums):
            if num not in val_hash:
                val_hash[num] = deque()
            val_hash[num].append(i)

            max_heap.push(num)
            if i + 1 < k:
                continue
            if i - k >= 0:
                slide_sta = i - k
                slide_end = i
                slide_out_num = nums[i - k]
                if max_heap.top() == slide_out_num:
                    max_heap.pop()
                    val_hash[slide_out_num].popleft()
                while True:
                    new_top = max_heap.top()
                    hash_idx = val_hash[new_top][0]
                    if hash_idx < slide_sta:
                        val_hash[new_top].popleft()
                        max_heap.pop()
                    else:
                        break

            result.append(max_heap.top())
            # print(result, val_hash)
        return result

data = [3, 2, 8, 3, 4, 2, 2, 2, 7, 7, 5, 2, 8, 9]
r = Solution().maxSlidingWindow(data, 5)
print(r)