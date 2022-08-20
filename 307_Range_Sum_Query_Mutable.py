from typing import List

class WeoBucket:
    def __init__(self, size):
        layer_idx = 0
        layer_size = 1
        self.layer_count = 1
        self.buckets = list[list[int]]()
        while size >= 0:
            layer_arr = [0] * layer_size
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

    def update(self, num, val):
        if num > self.size:
            return False
        layer_idx = self.layer_count - 1
        old_val = self.buckets[layer_idx][num]
        while layer_idx > 0:
            self.buckets[layer_idx][num] += val - old_val
            num >>= 1
            layer_idx -= 1

    def range_sum(self, start_num, end_num):
        start_sum = 0
        if start_num != 0:
            start_sum = self.acc_sum(start_num - 1)
        end_sum = self.acc_sum(end_num)
        return end_sum - start_sum

    def acc_sum(self, end_num) -> int:
        num = end_num + 1
        layer_idx = self.layer_count - 1
        result = 0
        while num > 0:
            # print(layer_idx, num, self.buckets[layer_idx][num - 1])
            if num & 1 == 1:
                result += self.buckets[layer_idx][num - 1]
            num >>= 1
            layer_idx -= 1
        return result

# b = WeoBucket(100)
# b.update(1, 5)
# b.update(2, 3)
# b.update(6, 4)
# print(b.buckets)
# print(b.acc_sum(6))
# print(b.range_sum(1, 6))


class NumArray:

    def __init__(self, nums: List[int]):
        self.bucket = WeoBucket(len(nums))
        for i, num in enumerate(nums):
            self.bucket.update(i, num)

    def update(self, index: int, val: int) -> None:
        self.bucket.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.bucket.range_sum(left, right)

arr = NumArray([1, 3, 5])
print(arr.sumRange(0, 2))
arr.update(1, 2)
print(arr.sumRange(0, 2))

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)