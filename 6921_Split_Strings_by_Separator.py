from typing import List

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            word_arr = word.split(sep=separator)
            for sep_word in word_arr:
                if sep_word != "":
                    ans.append(sep_word)

        return ans


data = [
    ["|aa||"]
    , "|"
]
r = Solution().splitWordsBySeparator(*data)
print(r)
