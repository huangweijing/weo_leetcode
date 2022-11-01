from typing import List
from collections import Counter

class Solution:
    def __init__(self):
        self.cnt = []
        self.arr = []
        self.result = 0
        self.one_group = dict[str, set[str]]()

    def calc_group(self):
        for i in range(len(self.arr)):
            self.one_group[self.arr[i]] = set[str]()
            for j in range(i + 1, len(self.arr)):
                if len(self.cnt[i] + self.cnt[j]) == len(self.arr[i]) + len(self.arr[j]):
                    self.one_group[self.arr[i]].add(self.arr[j])

    def calc_cnt(self):
        for s in self.arr:
            self.cnt.append(Counter(s))


    def my_max_len(self, word_len, candid: set[str]):
        if len(candid) == 0:
            self.result = max(self.result, word_len)
        else:
            for c in candid:
                new_candid = self.one_group[c] & candid
                self.my_max_len(word_len + len(c), new_candid)

    def maxLength(self, arr: List[str]) -> int:
        self.arr = arr
        self.calc_cnt()
        self.calc_group()
        for word in arr:
            if len(word) == len(set(word)):
                self.my_max_len(len(word), self.one_group[word])
        return self.result

data = ["aa","bb"]
r = Solution().maxLength(data)
print(r)