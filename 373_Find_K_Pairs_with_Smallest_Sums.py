import math
import heapq
from typing import List

class ObjectHeap:
    def __init__(self, key=lambda x: x):
        self.data = []
        self.key_func = key
        self.memory = dict[int, list[object]]()
        self.size = 0

    def top(self):
        if len(self.data) == 0:
            return None
        key = self.data[0]
        return self.memory[key][-1]

    def pop(self) -> object:
        key = self.data[0]
        obj = self.memory[key].pop()
        if len(self.memory[key]) == 0:
            del self.memory[key]
            heapq.heappop(self.data)
        self.size -= 1
        return obj

    def push(self, obj: object):
        key = self.key_func(obj)
        if key not in self.memory:
            self.memory[key] = []
            heapq.heappush(self.data, key)
        self.size += 1
        self.memory[key].append(obj)

    def length(self) -> int:
        return self.size

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ptr1, ptr2 = 0, 0
        result = []
        heap = ObjectHeap(lambda x : x[0] + x[1])
        heap.push([nums1[0], nums2[0], 0, 0])

        status = set[str]()
        status.add("0,0")

        while k > 0 and heap.length() > 0:
            k -= 1
            # print(heap.data, heap.memory)
            node = heap.pop()
            # print(f"node={node}, size={heap.length()}")
            result.append([node[0], node[1]])
            if node[2] + 1 < len(nums1) and f"{node[2] + 1},{node[3]}" not in status:
                new_node1 = [nums1[node[2] + 1], nums2[node[3]], node[2] + 1, node[3]]
                heap.push(new_node1)
                status.add(f"{node[2] + 1},{node[3]}")
            if node[3] + 1 < len(nums2) and f"{node[2]},{node[3] + 1}" not in status:
                new_node2 = [nums1[node[2]], nums2[node[3] + 1], node[2], node[3] + 1]
                heap.push(new_node2)
                status.add(f"{node[2]},{node[3] + 1}")

        return result



data = [[1,1,2]
, [1,2,3]
, 10
]
# data_num1 = [1,2]
# data_num2 = [3]
# data_k = 3
# r = Solution().kSmallestPairs(data_num1, data_num2, data_k)
r = Solution().kSmallestPairs(* data)
print(r)



