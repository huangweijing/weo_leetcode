from typing import List

class WordFilter:

    def __init__(self, words: List[str]):
        self.pre_table = dict[str, set[int]]()
        self.post_table = dict[str, set[int]]()
        dup_word_ht = dict[str, int]()
        for idx, word in enumerate(words):
            dup_word_ht[word] = idx

        for idx, word in enumerate(words):
            for i in range(len(word)):
                prefix = word[0: i + 1]
                postfix = word[i: len(word)]
                if prefix not in self.pre_table.keys():
                    self.pre_table[prefix] = set[int]()
                self.pre_table[prefix].add(dup_word_ht[word])
                if postfix not in self.post_table.keys():
                    self.post_table[postfix] = set[int]()
                self.post_table[postfix].add(dup_word_ht[word])

    def f(self, prefix: str, suffix: str) -> int:

        if prefix in self.pre_table.keys():
            set1 = self.pre_table[prefix]
        else:
            set1 = set[str]()
        if suffix in self.post_table.keys():
            set2 = self.post_table[suffix]
        else:
            set2 = set[str]()
        set3 = set1.intersection(set2)
        if len(set3) == 0:
            return -1
        return max(set3)


word_filter = WordFilter(["apple"])
r = word_filter.f("a", "e")
print(r)
