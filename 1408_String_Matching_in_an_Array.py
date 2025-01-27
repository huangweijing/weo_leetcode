from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set[str]()
        for word in words:
            for word2 in words:
                if word == word2:
                    continue
                if word2.find(word) != -1:
                    ans.add(word)
        return list(ans)
    

data = ["mass","as","hero","superhero"]
r = Solution().stringMatching(data)
print(r)
