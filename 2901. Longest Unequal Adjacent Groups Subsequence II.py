from typing import List
from collections import defaultdict
from functools import cache

class Solution:

    @cache
    def if_hamming_dist1(self, word1: str, word2: str):
        if len(word1) != len(word2):
            return False
        dist = 0
        for i, ch in enumerate(word1):
            if ch != word2[i]:
                dist += 1
            if dist >= 2:
                return False
        if dist == 1:
            return True
        return False

    def getWordsInLongestSubsequence(self, n: int, words: List[str]
                                     , groups: List[int]) -> List[str]:
        word_group = { words[i]: groups[i] for i in range(len(words)) }
        dp_words = defaultdict(lambda : list[str]())
        dp_words[words[0]].append(words[0])
        for i in range(1, n):
            new_dp_words = defaultdict(lambda : list[str]())
            if words[i] not in new_dp_words:
                new_dp_words[words[i]].append(words[i])
            for key, word_list in dp_words.items():
                if len(word_list) > len(new_dp_words[key]):
                    new_dp_words[key] = word_list
                if len(word_list) > 0 and self.if_hamming_dist1(word_list[-1], words[i]) \
                        and word_group[words[i]] != word_group[word_list[-1]]:
                    # if words[i] not in dp_words:
                    #     new_dp_words[words[i]] = [words[i]]
                    # else:
                    dp_word_list = new_dp_words[words[i]]
                    if len(word_list) + 1 > len(dp_word_list):
                        # if words[i] == "d":
                        #     print(word_list, dp_word_list, words[i], dp_words)
                        new_word_list = word_list.copy()
                        new_word_list.append(words[i])
                        new_dp_words[words[i]] = new_word_list

            # print(dp_words.items(), new_dp_words.items())
            dp_words = new_dp_words

        # print(dp_words)
        ans, max_len = [], 0
        for words_list in dp_words.values():
            if len(words_list) > 0:
                word_list_len = len(words_list)
                if word_list_len > max_len:
                    max_len = word_list_len
                    ans = words_list
        return ans


data = [
3
, ["bdb","aaa","ada"]
, [2,1,3]
]
r = Solution().getWordsInLongestSubsequence(*data)
print(r)