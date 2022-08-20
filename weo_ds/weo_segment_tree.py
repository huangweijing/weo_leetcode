class WeoSegmentTree:
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