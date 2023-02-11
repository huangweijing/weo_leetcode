from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = dict[str, int]()
        for i, ch in enumerate(order):
            mapping[order[i]] = i

        def cmp_word(w1: str, w2: str) -> int:
            word_len = min(len(w1), len(w2))
            for idx in range(word_len):
                if mapping[w1[idx]] < mapping[w2[idx]]:
                    return -1
                elif mapping[w1[idx]] > mapping[w2[idx]]:
                    return 1

            if len(w1) == len(w2):
                return 0
            elif len(w1) < len(w2):
                return -1
            else:
                return 1

        for i in range(len(words) - 1):
            cmp_result = cmp_word(words[i], words[i + 1])
            if cmp_result == 1:
                return False
        return True

data = [
    ["ubg","kwh"]
    , "qcipyamwvdjtesbghlorufnkzx"
]
r = Solution().isAlienSorted(* data)
print(r)