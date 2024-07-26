from typing import List


class Solution:
    def is_okay(self, s: str, dict_word: str) -> bool:
        idx1, idx2 = 0, 0
        while idx1 < len(s) and idx2 < len(dict_word):
            if s[idx1] == dict_word[idx2]:
                idx2 += 1
            if idx2 == len(dict_word):
                return True
            idx1 += 1
            # print(s[:idx2+1])
        return False


    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ans_word = ""
        dictionary.sort()
        for word in dictionary:
            if len(word) <= len(ans_word):
                continue
            # print(word, s, self.is_okay(s, word))
            if self.is_okay(s, word):
                ans_word = word
        return ans_word

# print("test",Solution().is_okay("abaaca", "aac"))

data = [
    "abpcplea"
    , ["ale","apple","monkey","plea"]
]
r = Solution().findLongestWord(*data)
print(r)
        