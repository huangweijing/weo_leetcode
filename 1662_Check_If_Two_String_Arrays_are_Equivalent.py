from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i, w1, ch1, w2, ch2 = 0, 0, 0, 0, 0
        while True:
            if word1[w1][ch1] != word2[w2][ch2]:
                return False
            i += 1
            ch1 += 1
            ch2 += 1
            if ch1 == len(word1[w1]):
                ch1 = 0
                w1 += 1
            if ch2 == len(word2[w2]):
                ch2 = 0
                w2 += 1
            if w1 == len(word1):
                break
            if w2 == len(word2):
                break

        if ch1 == 0 and ch2 == 0 and w1 == len(word1) and w2 == len(word2):
            return True
        return False

data = [["ab", "cd"]
    , ["abcd"]]
r = Solution().arrayStringsAreEqual(* data)
print(r)


