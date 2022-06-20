from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        rev_dic = set[str]()
        for word in words:
            for i in range(1, len(word)):
                rev_dic.add(word[i: len(word)])
        distinct_cnt = 0
        distinct_set = set[str]()
        total_len = 0
        for word in words:
            if word not in rev_dic and word not in distinct_set:
                distinct_cnt += 1
                total_len += len(word)
            distinct_set.add(word)

        return total_len + distinct_cnt

sol = Solution()
r = sol.minimumLengthEncoding(["time","time","time","time"])
print(r)
