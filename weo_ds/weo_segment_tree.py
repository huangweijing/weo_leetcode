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


from collections import Counter
class WeoSegTree:
    def __init__(self, size: int):
        self.size = 1 << size.bit_length() - 1
        self.nodes = Counter()

    def update_node(self, left: int, right: int, lo: int, hi: int, val:int, idx: int):
        print(f"left={left}, right={right}, lo={lo}, hi={hi}, val={val}, idx={idx}")
        if right < lo or hi < left:
            # print("if right < lo or hi < left:")
            return
        elif left <= lo <= hi <= right:
            # print("elif left <= lo <= hi <= right:")
            self.nodes[idx] = val
        else:
            mid = lo + hi >> 1
            self.update_node(left, right, lo, mid, val, (idx << 1) + 1)
            self.update_node(left, right, mid + 1, hi, val, (idx << 1) + 2)

    def update(self, left:int, right: int, val:int):
        self.update_node(left, right, 0, self.size, val, 0)

    def get_node(self, num: int, lo:int, hi: int, idx: int) -> int:
        print(f"num={num}, lo={lo}, hi={hi}, idx={idx}, val={self.nodes[idx]}")
        if num < lo or num > hi:
            return None
        if lo <= num <= hi:
            if self.nodes[idx] == 0:
                mid = lo + hi >> 1
                if num <= mid:
                    return self.get_node(num, lo, mid, (idx << 1) + 1)
                else:
                    return self.get_node(num, mid + 1, hi, (idx << 1) + 2)
            else:
                return self.nodes[idx]

    def get(self, num: int) -> int:
        return self.get_node(num, 0, self.size, 0)

wst = WeoSegTree(1000)
wst.update(4, 160, 5)
print(wst.nodes)
# print(f"wst.get(100)={wst.get(100)}")
wst.update(120, 175, 10)
print(wst.nodes)
# print(f"wst.get(119)={wst.get(119)}")
# print(f"wst.get(120)={wst.get(120)}")
# print(f"wst.get(121)={wst.get(121)}")
# print(f"wst.get(170)={wst.get(170)}")
