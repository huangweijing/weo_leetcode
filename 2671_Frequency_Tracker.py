from collections import Counter


class FrequencyTracker:

    def __init__(self):
        self.num_cnt = Counter()
        self.freq_cnt = Counter()

    def add(self, number: int) -> None:
        if self.num_cnt[number] != 0:
            self.freq_cnt[self.num_cnt[number]] -= 1
        self.num_cnt[number] += 1
        self.freq_cnt[self.num_cnt[number]] += 1
        # print(f"add({number}): freq_cnt={self.freq_cnt}, num_cnt={self.num_cnt}")

    def deleteOne(self, number: int) -> None:
        if self.num_cnt[number] == 0:
            # print(f"delete({number}): freq_cnt={self.freq_cnt}, num_cnt={self.num_cnt}")
            return
        self.freq_cnt[self.num_cnt[number]] -= 1
        if self.freq_cnt[self.num_cnt[number]] == 0:
            del self.freq_cnt[self.num_cnt[number]]
        self.num_cnt[number] -= 1
        if self.num_cnt[number] > 0:
            self.freq_cnt[self.num_cnt[number]] += 1
        # print(f"delete({number}): freq_cnt={self.freq_cnt}, num_cnt={self.num_cnt}")

    def hasFrequency(self, frequency: int) -> bool:
        # print(f"freq: freq_cnt={self.freq_cnt}, num_cnt={self.num_cnt}")
        return self.freq_cnt[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)