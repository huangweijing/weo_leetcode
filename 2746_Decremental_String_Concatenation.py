from typing import List
from collections import defaultdict
import math

class Solution:
    def __init__(self):
        self.words = []

    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        self.words = words
        dp_dict = defaultdict(lambda : math.inf)
        dp_dict[words[0][0] + words[0][-1]] = len(words[0])
        for i, word in enumerate(words[1:]):
            new_dp_dict = defaultdict(lambda : math.inf)
            for dp_key in dp_dict:
                new_dp_key = word[0] + dp_key[-1]
                if dp_key[0] == word[-1]:
                    new_dp_dict[new_dp_key] = min(dp_dict[dp_key] + len(word) - 1
                                                  , new_dp_dict[new_dp_key])
                else:
                    new_dp_dict[new_dp_key] = min(dp_dict[dp_key] + len(word)
                                                  , new_dp_dict[new_dp_key])

                new_dp_key = dp_key[0] + word[-1]
                if dp_key[-1] == word[0]:
                    new_dp_dict[new_dp_key] = min(dp_dict[dp_key] + len(word) - 1
                                                  , new_dp_dict[new_dp_key])
                else:
                    new_dp_dict[new_dp_key] = min(dp_dict[dp_key] + len(word)
                                                  , new_dp_dict[new_dp_key])

            dp_dict = new_dp_dict

        return min(dp_dict.values())

data = ["aa","ab","bc"]
r = Solution().minimizeConcatenatedLength(data)
print(r)





