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

    def get_interval_list(self):


    def print(self):
        for layer in self.buckets:
            print(layer)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
