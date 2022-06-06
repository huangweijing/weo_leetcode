from typing import List

class WeoBucket:
    def __init__(self, size):
        layer_idx = 0
        layer_size = 1
        self.layer_count = 1
        self.buckets = list[list[bool]]()
        while size >= 0:
            layer_arr = [False] * layer_size
            self.buckets.append(layer_arr)
            # print(layer_size)
            if size == 0:
                break
            layer_size <<= 1
            layer_idx += 1
            size >>= 1
        self.layer_count = layer_idx + 1
        self.size = len(self.buckets[layer_idx])

        # print(f"size={self.size}")

    def add(self, num):
        if num > self.size:
            return False
        layer_idx = self.layer_count - 1
        self.buckets[layer_idx][num] = True
        while layer_idx > 0:
            sec_start_idx = (num >> 1) << 1
            if self.buckets[layer_idx][sec_start_idx] and self.buckets[layer_idx][sec_start_idx + 1]:
                self.buckets[layer_idx - 1][num >> 1] = True
            num >>= 1
            layer_idx -= 1

    def remove(self, num):
        if num > self.size:
            return False
        layer_idx = self.layer_count - 1
        self.buckets[layer_idx][num] = False
        while layer_idx > 0:
            sec_start_idx = (num >> 1) << 1
            if not(self.buckets[layer_idx][sec_start_idx] and self.buckets[layer_idx][sec_start_idx + 1]):
                self.buckets[layer_idx - 1][num >> 1] = False
            num >>= 1
            layer_idx -= 1

    def get_first_missing_positive(self):
        if self.buckets[0][0]:
            return -1

        layer_idx = 1
        first_false_idx = 0
        while layer_idx < self.layer_count:
            layer = self.buckets[layer_idx]
            offset = 1 if layer[first_false_idx] else 0
            first_false_idx = first_false_idx + offset
            # print(first_false_idx)
            if layer_idx == self.layer_count - 1:
                break
            first_false_idx <<= 1
            layer_idx += 1
        return first_false_idx

    def print(self):
        for layer in self.buckets:
            print(layer)


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        weo_bucket = WeoBucket(5 * (10**5))
        weo_bucket.add(0)
        for num in nums:
            if num > 0:
                weo_bucket.add(num)
        return weo_bucket.get_first_missing_positive()

data = [1,2,0]
sol = Solution()
r = sol.firstMissingPositive(data)
print(r)

# bucket = WeoBucket(100000)
# for i in range(100000):
#     bucket.add(i)
# bucket.remove(4329)
# bucket.remove(4129)
# # bucket.print()
# print(bucket.get_first_missing_positive())

# print(list(range(0, 0)))