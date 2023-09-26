import heapq
from functools import cmp_to_key
from collections import Counter, defaultdict
from sortedcontainers import SortedList

class FreqStack:

    def __init__(self):
        self.id = 0
        self.freq_dict = Counter()
        self.num_pos = defaultdict(lambda: list[int]())
        self.freq_num = defaultdict(lambda: SortedList())
        self.freq_order = SortedList()

    def push(self, val: int) -> None:
        self.id += 1
        if val not in self.freq_dict:
            self.freq_dict[val] = 1
            self.num_pos[val].append(self.id)
            if 1 not in self.freq_num:
                self.freq_order.add(1)
            self.freq_num[1].add(val)
        else:
            freq = self.freq_dict[val]
            self.freq_dict[val] = freq + 1
            self.num_pos[val].append(self.id)

            self.freq_num[freq].remove(val)
            if len(self.freq_num[freq]) == 0:
                del self.freq_num[freq]
                self.freq_order.remove(freq)

            self.freq_num[freq + 1].add(val)
            if len(self.freq_num[freq + 1]) == 1:
                self.freq_order.add(freq + 1)

    def pop(self) -> int:
        freq = self.freq_order[-1]
        max_id = -1
        num_to_pop = -1
        # define num
        for num in self.freq_num[freq]:
            if self.num_pos[num][-1] > max_id:
                num_to_pop = num
                max_id = self.num_pos[num][-1]
        # remove from freq num
        self.freq_num[freq].remove(num_to_pop)
        if len(self.freq_num[freq]) == 0:
            del self.freq_num[freq]
        # update freq - 1
        if freq - 1 > 0:
            self.freq_num[freq - 1].add(num_to_pop)
        # delete the latest one
        self.num_pos[num_to_pop].pop()
        # delete freq dict
        self.freq_dict[num_to_pop] -= 1
        if self.freq_dict[num_to_pop] == 0:
            del self.freq_dict[num_to_pop]
        # update freq order
        if len(self.freq_num[freq]) == 0:
            self.freq_order.remove(freq)
        if len(self.freq_num[freq - 1]) == 1:
            self.freq_order.add(freq - 1)
        return num_to_pop

# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
obj.push(3)
obj.push(5)
obj.push(3)
print(obj.pop())
print(obj.pop())
print(obj.pop())